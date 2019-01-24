import model
from para import *

def main():
    md = model.Model()

    md.load()

    md.train(epochs=EPOCHS)


if __name__ == '__main__':
    main()