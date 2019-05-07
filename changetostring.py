import numpy as np
from createfield import Field


class ChangeToString():
    def __init__(self, booleanfield):
        self.__booleanfield = booleanfield

    def get_stringfiled(self):
        self.__buffiled = np.where(self.__booleanfield == 1, '■', '□')
        return self.__buffiled


if __name__ == "__main__":
    basefield = Field()
    bufield = ChangeToString(basefield.get_room())
    print(bufield.get_stringfiled())
