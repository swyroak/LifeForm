from lifecycle import basecycle
from createfield import ConstFiled
from imaging import ImagingObjct
from PIL import Image
import os
import pathlib


def createimg():
    p_temp = pathlib.Path('static')
    for p in p_temp.glob('temp*'):
        os.remove('static/' + p.name)

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
        images.append(ImagingObjct(bufcycle, height, width).get_img())
    dname = 'static/tempimg.gif'
    img.save(dname, save_all=True,
             append_images=images[1:], optimize=False, duration=100, loop=0)


if __name__ == "__main__":
    createimg()
