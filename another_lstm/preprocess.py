# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function
import pandas as pd
import jieba, jieba.analyse
import numpy as np
from para import *

class Data():

    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.content = None
        self.sentence = None
        self.chars = None
        self.char2idx = None
        self.idx2char = None
        self.get_chars()

    def load(self):
        data = pd.read_csv(self.filename)
        data = data.dropna()
        del data['date']
        del data['tag']
        return data  

    def get_content(self):
        """
        获取所有内容拼接起来的字符串
        """
        if self.content is None:
            data = self.get_data()
            self.content = ''.join([data.iloc[i]['content'].strip() for i in range(len(data))])
        return self.content

    def get_sentence(self):
        """
        获取所有句子，[['我','今天','很高兴','。'], ...]
        """
        if self.sentence is None:
            data = self.get_data()
            data['sentence'] = data.apply(lambda x: self.cut_sent(x['content']), axis=1)
            sentence = [s for lst in data['sentence'].tolist() for s in lst]
            self.sentence = sorted(sentence, key=len)
        return self.sentence

    def get_data(self):
        if self.data is None:
            self.data = self.load()
        return self.data

    def get_words(self, top):
        """
        获取频率最高的 top 个词语
        """

        try:
            with open('words.txt', 'r') as f:
                words = [line.strip() for line in f.readlines()]
        except IOError:
            content = self.get_content()
            words = pd.DataFrame([w for w in jieba.cut(content)], 
                            columns=['words'])
            freq = words['words'].value_counts()
            
            words = sorted(freq.keys(), key=lambda x:-freq[x])[:top]

            with open('words.txt', 'w') as f:
                for w in words:
                    f.write(w)
                    f.write('\n')

        return words

    def get_chars(self):
        """
        获取频率最高的 top 个字符
        """

        if self.chars is None:
            words = self.get_words(CHAR_SIZE-2)
            # chars = pd.DataFrame([c for word in words for c in word], 
            #                 columns=['chars'])
            # freq = chars['chars'].value_counts()
            # self.chars = freq.keys()
            self.chars = words
            self.chars.append(UNK)
            print('chars:', self.chars[:100])
        return self.chars

    def get_char2idx(self, char):
        if self.char2idx is None:
            self.char2idx = {word:i for i, word in enumerate(self.get_chars())}
        
        if char in self.char2idx:
            return self.char2idx[char]
        return self.char2idx[UNK]
    
    def get_idx2char(self, idx):
        if self.idx2char is None:
             self.idx2char = np.array(self.get_chars())
    
        return self.idx2char[idx]

    def cut_sent(self, sentences):
        words = self.get_chars()
        import re
        # 待删去的高频无效短语
        noises = ['————–', '\xa0\xa0\xa0', '，', '、', ' ', '　', '（', '）']
        # 根据标点符号断句，引号前的标点符号不断
        sentences = re.sub('([。！？；\?])([^”’])', r"\1\n\2", sentences).strip().split("\n")
        res = []
        for sen in sentences:
            # 将无效的换为分隔符
            for noise in noises:
                sen = sen.replace(noise, '，')
            new_sen = []
            # 先按分隔符划分短语，去除无效的内容
            for short in sen.split('，'):
                if len(short) < 4: # 人名一般长度为3
                    continue
                # 将数字换为0
                new_short = ''
                begin = False
                for idx, char in enumerate(short):
                    if char in '0123456789':
                        if not begin:
                            begin = True
                            new_short += '0'
                    else:
                        new_short += char
                        begin = False
                if new_short in words:
                    new_sen.append(new_short)
            new_sen = "，".join(new_sen)
            if new_sen != '' and len(new_sen) < MAX_LEN_SEN:
                res.append(new_sen)
        
        return res  