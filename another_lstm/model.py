# -*- coding:utf-8 -*- 
import tensorflow as tf
tf.enable_eager_execution()
import numpy as np
import os
import time
from preprocess import Data
from para import *

class Model():

    def __init__(self, datafile="chinese_news.csv", checkpoint_dir='./training_checkpoints'):
        self.model = None
        self.checkpoint_dir = checkpoint_dir
        self.data = Data(datafile)
        self.dataset = None

    def build(self, batch_size):
        self.batch_size = batch_size
        if tf.test.is_gpu_available():
            rnn = tf.keras.layers.CuDNNLSTM
        else:
            import functools
            rnn = functools.partial(
                tf.keras.layers.LSTM, recurrent_activation='relu')

        self.model = tf.keras.Sequential([
            # Embedding
            tf.keras.layers.Embedding(CHAR_SIZE, EMBEDDING_DIM, 
                                    batch_input_shape=[batch_size, None]),
            # Bidirectional LSTM
            tf.keras.layers.Bidirectional(rnn(RNN_UNITS,
                return_sequences=True, 
                recurrent_initializer='glorot_uniform',
                stateful=True)),
            # Dropout
            tf.keras.layers.Dropout(DROPOUT_RATE), 

            # Dense
            tf.keras.layers.Dense(CHAR_SIZE, activation='softmax')
        ])

    def input_fn(self, file_path):
        def parse(example_proto):
            features = {"idx_lst": tf.VarLenFeature(tf.int64)}
            parsed_features = tf.parse_single_example(example_proto, features)
            idx_lst = tf.sparse.to_dense(parsed_features["idx_lst"])
            idx_lst = tf.cast(idx_lst, tf.int32)
            return idx_lst[:-1], idx_lst[1:]

        dataset = (tf.data.TFRecordDataset(file_path).map(parse))
        if SHUFFLE:
            dataset = dataset.shuffle(buffer_size=BUFFER_SIZE)
        dataset = dataset.repeat()
        return dataset.padded_batch(BATCH_SIZE, padded_shapes=([MAX_LEN_SEN-1], [MAX_LEN_SEN-1]))

    def get_dataset(self):
        if self.dataset is None:
            char2idx = self.data.get_char2idx
            sentences = self.data.get_sentence()
            with tf.python_io.TFRecordWriter(TRAIN_RECORD_FILE) as writer:
                for sen in sentences:
                    idx_lst = [char2idx(c) for c in sen]
                    example = tf.train.Example(features=tf.train.Features(feature={
                        'idx_lst': tf.train.Feature(int64_list=tf.train.Int64List(value=idx_lst))
                    }))
                    writer.write(example.SerializeToString())

            self.dataset = self.input_fn(TRAIN_RECORD_FILE)
        
        return self.dataset

    def train(self, epochs=3):

        def loss(labels, logits):
            return tf.keras.losses.sparse_categorical_crossentropy(labels, logits)

        self.model.compile(optimizer = tf.train.AdamOptimizer(),
                        loss = loss)

        checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
            filepath=os.path.join(self.checkpoint_dir, "ckpt_{epoch}"),
            save_weights_only=True)

        dataset = self.get_dataset()

        history = self.model.fit(dataset, 
                            epochs=epochs, 
                            steps_per_epoch=MAX_LEN_SEN, 
                            callbacks=[checkpoint_callback])
        return history
 
    def load(self):
        try:
            tf.train.latest_checkpoint(self.checkpoint_dir)
            self.build(batch_size=1)

            self.model.load_weights(tf.train.latest_checkpoint(self.checkpoint_dir))

            self.model.build(tf.TensorShape([1, None]))

        except:
            self.build(batch_size=BATCH_SIZE)

    def predict(self, start_string, generate_size=1000):
        char2idx = self.data.get_char2idx
        idx2char = self.data.get_idx2char

        # Converting our start string to numbers (vectorizing) 
        input_eval = [char2idx(s) for s in start_string]
        input_eval = tf.expand_dims(input_eval, 0)
        text_generated = []

        # Low temperatures results in more predictable text.
        # Higher temperatures results in more surprising text.
        # Experiment to find the best setting.
        temperature = 1.0

        # Here batch size == 1
        self.model.reset_states()
        
        for i in range(generate_size):

            if np.random.rand() < PUNCTUATION_RATE:
                if np.random.rand() < 0.5:
                    text_generated.append('，')
                else:
                    text_generated.append('。')

            predictions = self.model(input_eval)
            # remove the batch dimension
            predictions = tf.squeeze(predictions, 0)

            # using a multinomial distribution to predict the word returned by the model
            predictions = predictions / temperature
            predicted_id = tf.multinomial(predictions, num_samples=1)[-1,0].numpy()
            
            # We pass the predicted word as the next input to the model
            # along with the previous hidden state
            input_eval = tf.expand_dims([predicted_id], 0)
            nchar = idx2char(predicted_id)
            if nchar == UNK:
                print(' ')
            text_generated.append(nchar)
        return (start_string + ''.join(text_generated))
