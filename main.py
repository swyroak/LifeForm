from changetostring import ChangeToString
from lifecycle import basecycle
from createfield import ConstFiled
from flask import render_template
from flask import Flask
import numpy as np
app = Flask(__name__)


@app.route('/')
def hello():
    basefield = ConstFiled(50, 50)
    cycles = []
    strcycles = []
    arycycles = []
    buffiled = basecycle(basefield.get_room())
    cycles.append(buffiled)
    strcycles.append(ChangeToString(cycles[0]).get_stringfiled())
    for i in range(300):
        bufcycle = basecycle(cycles[i])
        bufarycycle = bufcycle.tolist()
        bufstrcycle = ChangeToString(bufcycle).get_stringfiled().tolist()
        cycles.append(bufcycle)
        arycycles.append(bufarycycle)
        strcycles.append(bufstrcycle)

    return render_template('main.html', cycles=strcycles, name="a")


if __name__ == "__main__":
    #app.run(debug=True)
    # app.run('0.0.0.0',port=8080)
    hello()