from PIL import Image, ImageDraw
from createfield import ConstFiled
# import os
# import tempfile
# import random


class ImagingObjct():
    def __init__(self, fieldS, height, width):
        self.__height = height * 4 + 1
        self.__Width = width * 4 + 1
        self.__img = Image.new('RGB', (self.__Width, self.__height))
        # self.__img.show()
        self.__draw = ImageDraw.Draw(self.__img)
        i = 1
        j = 1
        for field in fieldS:
            for fieldobj in field:
                if fieldobj:
                    self.__draw.rectangle(
                        [i, j, i + 2, j + 2], fill='White')
                # else:
                #    self.__draw.rectangle(
                #        [i, j, i + 4, j + 4], fill='Black', outline='White')
                i += 4
            i = 1
            j += 4
        # self.__img.show()
        # savename = 'dev' + str(random.randrange(1, 100000))
        # self.__img.save(savename + '.jpg', quality=50)

    def get_img(self):
        # self.__img.show()
        return self.__img


if __name__ == "__main__":
    fld = ConstFiled(50, 50)
    objimage = ImagingObjct(fld.get_room(), fld.get_height(), fld.get_width())
    h = objimage.get_img()
    h.show()
