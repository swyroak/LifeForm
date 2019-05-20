from lifecycle import basecycle
from createfield import ConstFiled
from imaging import ImagingObjct
from PIL import Image
import os
import sys
import shutil


def createimg():
    if sys.platform == 'darwin':
        imgpath = 'static/imgs'
        if os.path.exists(imgpath):
            shutil.rmtree(imgpath)
            os.mkdir(imgpath)
        else:
            os.mkdir(imgpath)
    else:
        imgpath = '/var/www/LifeFrom/static/imgs'
        if os.path.exists(imgpath):
            shutil.rmtree(imgpath)
            os.mkdir(imgpath)
        else:
            os.mkdir(imgpath)

    height = 50
    width = 50
    basefield = ConstFiled(height, width)
    cycles = []
    arycycles = []
    images = []
    buffiled = basecycle(basefield.get_room())
    cycles.append(buffiled)
    img = Image.new('RGB', (height * 4 + 1, width * 4 + 1))
    images.append(ImagingObjct(buffiled, height, width).get_img())
    for i in range(500):
        bufcycle = basecycle(cycles[i])
        bufarycycle = bufcycle.tolist()
        cycles.append(bufcycle)
        arycycles.append(bufarycycle)
        bufimg = ImagingObjct(bufcycle, height, width).get_img()
        images.append(bufimg)
        bufimgname = 'static/imgs/img' + str(i) + '.jpg'
        bufimg.save(bufimgname, format='jpeg')

    if sys.platform == 'darwin':
        dname = 'static/imgs/tempimg.gif'
    else:
        dname = '/var/www/LifeFrom/tempimg.gif'
    img.save(dname, save_all=True,
             append_images=images[1:], optimize=False, duration=100, loop=0)


if __name__ == "__main__":
    createimg()
