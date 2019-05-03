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
    buffiled = basecycle(basefield.get_room())
    buffiled = ChangeToString(buffiled)
    cycles.append(buffiled.returnstringfiled)
    for i in range(11):
        cycles.append(basecycle(cycles[i]))
    for cycle in cycles:
        print(cycle)
    return render_template('main.html', cycles=cycles)


if __name__ == "__main__":
    app.run(debug=True)
