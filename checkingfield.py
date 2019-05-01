import numpy as np


class Checkingfield():
    """
    checking a quentity of neigberfoodcell
    """

    def __init__(self, field):
        self.__field = field
        self.__frow = field.shape[0]
        self.__fcol = field.shape[1]

    def get_field(self):
        return self.__field

    def get_frow(self):
        return self.__frow

    def get_fcol(self):
        return self.__fieldlcol

    def get_slicing_top(self):
        return self.__slicing_top

    def get_slicing_lft(self):
        return self.__slicing_lft

    def get_slicing_btm(self):
        return self.__slicing_btm

    def get_slicing_rgt(self):
        return self.__slicing_rgt

    def get_slicing_toplft(self):
        return self.__slicing_toplft

    def get_slicing_btmlft(self):
        return self.__slicing_btmlft

    def get_slicing_toprgt(self):
        return self.__slicing_toprgt

    def get_slicing_btmrgt(self):
        return self.__slicing_btmrgt

    def get_summaryslicedfields(self):
        return self.get_slicing_top() + self.get_slicing_lft() \
            + self.get_slicing_btm() + self.get_slicing_rgt() \
            + self.get_slicing_toplft() + self.get_slicing_btmlft() \
            + self.get_slicing_toprgt() + self.get_slicing_btmrgt()

    def slicing_top(self):
        self.__slicing_top = self.slicing_filed(1, 0, 0, 0)

    def slicing_lft(self):
        self.__slicing_lft = self.slicing_filed(0, 0, 1, 0)

    def slicing_btm(self):
        self.__slicing_btm = self.slicing_filed(0, 1, 0, 0)

    def slicing_rgt(self):
        self.__slicing_rgt = self.slicing_filed(0, 0, 0, 1)

    def slicing_toplft(self):
        self.__slicing_toplft = self.slicing_filed(1, 0, 1, 0)

    def slicing_btmlft(self):
        self.__slicing_btmlft = self.slicing_filed(0, 1, 1, 0)

    def slicing_toprgt(self):
        self.__slicing_toprgt = self.slicing_filed(1, 0, 0, 1)

    def slicing_btmrgt(self):
        self.__slicing_btmrgt = self.slicing_filed(0, 1, 0, 1)

    def slicing_all(self):
        self.__slicing_top = self.slicing_filed(1, 0, 0, 0)
        self.__slicing_lft = self.slicing_filed(0, 0, 1, 0)
        self.__slicing_btm = self.slicing_filed(0, 1, 0, 0)
        self.__slicing_rgt = self.slicing_filed(0, 0, 0, 1)
        self.__slicing_toplft = self.slicing_filed(1, 0, 1, 0)
        self.__slicing_btmlft = self.slicing_filed(0, 1, 1, 0)
        self.__slicing_toprgt = self.slicing_filed(1, 0, 0, 1)
        self.__slicing_btmrgt = self.slicing_filed(0, 1, 0, 1)

    def slicing_filed(self, strtrow, endrow, strtcol, endcol):

        self.__bufslc = self.__field[strtrow:self.__frow -
                                     endrow, strtcol:self.__fcol - endcol]

        if strtrow + endrow > 0:
            self.__adcol = np.zeros(self.__bufslc.shape[1], dtype="int64")
            self.__adcol = np.reshape(self.__adcol, (1, self.__adcol.shape[0]))
            if strtrow == 0:
                self.__bufslc = np.vstack((self.__adcol, self.__bufslc))
            else:
                self.__bufslc = np.vstack((self.__bufslc, self.__adcol))

        if strtcol + endcol > 0:
            self.__adrow = np.zeros(self.__bufslc.shape[0], dtype="int64")
            self.__adrow = np.reshape(self.__adrow, (self.__adrow.shape[0], 1))
            if strtcol == 0:
                self.__bufslc = np.hstack((self.__adrow, self.__bufslc))
            else:
                self.__bufslc = np.hstack((self.__bufslc, self.__adrow))

        return self.__bufslc


if __name__ == "__main__":
    test = Checkingfield(np.random.randint(0, 2, (5, 10)))
    print("元々ーーーーーーーーーーーーーーーーーーーーーーーーーーー")
    print(test.get_field())
    print("上ズレーーーーーーーーーーーーーーーーーーーーーーーーーーー")
    print(test.slicing_top())
    print(test.get_slicing_top())
    print("左ズレーーーーーーーーーーーーーーーーーーーーーーーーーーー")
    print(test.slicing_lft())
    print(test.get_slicing_lft())
    print("下ズレーーーーーーーーーーーーーーーーーーーーーーーーーーー")
    print(test.slicing_btm())
    print(test.get_slicing_btm())
    print("右ズレーーーーーーーーーーーーーーーーーーーーーーーーーーー")
    print(test.slicing_rgt())
    print(test.get_slicing_rgt())
    print("上左ズレーーーーーーーーーーーーーーーーーーーーーーーーーーー")
    print(test.slicing_toplft())
    print(test.get_slicing_toplft())
    print("下左ズレーーーーーーーーーーーーーーーーーーーーーーーーーーー")
    print(test.slicing_btmlft())
    print(test.get_slicing_btmlft())
    print("上右ズレーーーーーーーーーーーーーーーーーーーーーーーーーーー")
    print(test.slicing_toprgt())
    print(test.get_slicing_toprgt())
    print("下右ズレーーーーーーーーーーーーーーーーーーーーーーーーーーー")
    print(test.slicing_btmrgt())
    print(test.get_slicing_btmrgt())
    print("合計ーーーーーーーーーーーーーーーーーーーーーーーーーーー")
    print(test.get_summaryslicedfields())
    print("END")
