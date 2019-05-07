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
    bufcycles = []
    buffiled = basecycle(basefield.get_room())
    cycles.append(buffiled)
    bufcycles.append(ChangeToString(cycles[0]).get_stringfiled())
    for i in range(300):
        cycles.append(basecycle(cycles[i]))
        bufcycles.append(ChangeToString(cycles[i]).get_stringfiled())
    print(bufcycles)
    print(cycles)

    return render_template('main.html', cycles=cycles, name="a")


if __name__ == "__main__":
    hello()
    # app.run(debug=True)
    # app.run('0.0.0.0',port=8080)
