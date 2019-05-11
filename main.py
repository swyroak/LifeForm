from lifecycle import basecycle
from createfield import ConstFiled
from flask import render_template
from flask import Flask
from imaging import ImagingObjct
from PIL import Image, ImageDraw

app = Flask(__name__)


@app.route('/')
def hello():
    basefield = ConstFiled(50, 50)
    cycles = []
    arycycles = []
    images = []

    buffiled = basecycle(basefield.get_room())
    height = basefield.get_height()
    width = basefield.get_width()
    cycles.append(buffiled)
    img = Image.new('RGB', (height, width))
    images.append(ImagingObjct(buffiled, height, width).sss())
    for i in range(300):
        bufcycle = basecycle(cycles[i])
        bufarycycle = bufcycle.tolist()
        cycles.append(bufcycle)
        arycycles.append(bufarycycle)
        images.append(ImagingObjct(bufcycle, height, width).sss())
    img.save('img.gif', save_all=True, append_images=images[1:],
             optimize=False, duration=40, loop=0)
    return render_template('main.html', cycles=arycycles, name="a")


if __name__ == "__main__":
    # app.run(debug=True)
    # app.run('0.0.0.0',port=8080)
    hello()
