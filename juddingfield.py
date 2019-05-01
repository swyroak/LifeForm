import numpy as np


class juddingfield():
    """

    """

    def __init__(self, field, thenfield):
        self.__field = field
        self.__thenfield = thenfield

    def judging_life(self):
        self.__futurefield = np.where(
            self.__field == 3, True, self.__thenfield)
        self.__futurefield = np.where(
            self.__field <= 1, False, self.__futurefield)
        self.__futurefield = np.where(
            self.__field >= 4, False, self.__futurefield)

    def get_futurefield(self):
        return self.__futurefield

    def get_dic(self):
        return self.__dic
