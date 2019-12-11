from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html', name='Channing!')

@app.route('/graph')
def graph():
    return render_template("hello.html", Test="Channing!")

if __name__ == '__main__':
    app.run(debug=True)
