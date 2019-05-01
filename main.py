from flask import Flask
from flask import render_template
from createfield import Field
from lifecycle import basecycle

app = Flask(__name__)


@app.route('/')
def hello(name=None):
    basefield = Field()
    cycles = []
    cycles.append(basecycle(basefield.get_room()))
    for i in range(11):
        cycles.append(basecycle(cycles[i]))
    for cycle in cycles:
        print(cycle)
    return render_template('main.html', name=name, cycles=20)


if __name__ == "__main__":
    app.run(debug=True)
