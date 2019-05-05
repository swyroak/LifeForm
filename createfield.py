import numpy as np
import random as rnd


class Field():
    def __init__(self):
        self.__height = self.__decide_height()
        self.__width = self.__decide_width()
        self.__room = np.random.randint(
            0, 2, (self.get_height(), self.get_width()))

    def __decide_height(self):
        return rnd.randint(1, 5) * 2

    def __decide_width(self):
        return rnd.randint(1, 8) * 2

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def get_room(self):
        return self.__room


class ConstFiled():
    def __init__(self, rowsize, colsize):
        self.__height = rowsize
        self.__width = colsize
        self.__room = np.random.randint(
            0, 2, (self.get_height(), self.get_width()))

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def get_room(self):
        return self.__room


if __name__ == "__main__":
    fieldobjcet = Field()
    print(fieldobjcet.get_room())
    constfieldobject = ConstFiled(50, 50)
    print(constfieldobject.get_room())
