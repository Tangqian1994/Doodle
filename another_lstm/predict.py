# -*- coding:utf-8 -*- 
import model

md = model.Model()
md.load()

def main():
    while True:
        start = input('Please input start string:')
        step = int(input('Please input length of text to generate:'))
        prediction = md.predict(start, step)
        print('Prediction: ', prediction)

def get_prediction(start, step=100):
    return md.predict(start, step)


if __name__ == '__main__':
    main()
    
    