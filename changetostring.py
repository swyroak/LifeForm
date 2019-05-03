import numpy as np


class ChangeToString():
    def __init__(self, booleanfield):
        self.__booleanfield = booleanfield

    def returnstringfiled(self):
        self.__buffiled = np.where(self.__booleanfield == 1, "■", "  ")
        return self.__buffiled
