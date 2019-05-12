from lifecycle import basecycle
from createfield import ConstFiled
from flask import render_template
from flask import Flask
from imaging import ImagingObjct
from PIL import Image
import datetime
import random
import shutil
import os
import pathlib


app = Flask(__name__)


@app.route('/')
def hello():
    p_temp = pathlib.Path('static')
    for p in p_temp.glob('temp*'):
        shutil.rmtree('static/' + p.name)

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
    dname = 'static/temp' + datetime.datetime.today().strftime('%Y%m%d%H%M%S%f') + \
        str(random.randint(1, 9999))
    os.mkdir(dname)
    img.save(dname + '/img.gif', save_all=True,
             append_images=images[1:], optimize=False, duration=100, loop=0)
    return render_template('main.html', dname=dname + '/img.gif', name="a")


if __name__ == "__main__":
    app.run(debug=True)
    # app.run('0.0.0.0',port=8080)
    # hello()
