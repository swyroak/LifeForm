from flask import render_template
from flask import Flask
import createimg
import sys
app = Flask(__name__)


@app.route('/')
def hello():
    createimg.createimg()
    return render_template('main.html', name="a")


if __name__ == "__main__":
    if sys.platform == 'darwin':
        app.run(debug=True)
    else:
        app.run('0.0.0.0', port=8080)
