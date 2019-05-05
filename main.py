from flask import Flask
from flask import render_template
from createfield import Field
from lifecycle import basecycle
from changetostring import ChangeToString
app = Flask(__name__)


@app.route('/')
def hello():
    basefield = Field()
    cycles = []
    bufcycles = []
    buffiled = basecycle(basefield.get_room())
    cycles.append(buffiled)
    bufcycles.append(ChangeToString(cycles[0]).get_stringfiled())
    for i in range(5):
        cycles.append(basecycle(cycles[i]))
        bufcycles.append(ChangeToString(cycles[i]).get_stringfiled())
    print(bufcycles)
    print(cycles)

    return render_template('main.html', cycles=bufcycles)


if __name__ == "__main__":
    app.run(debug=True)
