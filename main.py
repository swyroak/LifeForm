from flask import Flask, render_template, request
import createimg
import sys
app = Flask(__name__)


@app.route('/')
def hello():
    # createimg.createimg()
    return render_template('main.html', gens=30)


@app.route('/restart', methods=['GET', 'POST'])
def hello2(gens):
    # gens=request.args.get()
    print(gens)
    createimg.createimg(30)
    return render_template('main.html', gens=30)


if __name__ == "__main__":
    if sys.platform == 'darwin':
        app.run(debug=True)
    else:
        app.run('0.0.0.0', port=8080)
