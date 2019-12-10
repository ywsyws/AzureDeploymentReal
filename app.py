import io
import pandas as pd
import pyodbc
from flask import Flask
from flask import render_template
from flask import Response
from graph import create_figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html', name='Channing!')


@app.route('/plot.png')
def plot():

    conn = pyodbc.connect(
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=azuresqlorange.database.windows.net;'
        'Database=orange_azure;'
        'Trusted_Connectoin=yes;'
        'UID=orange;'
        'PWD=Supermotdepasse!42;')
    cursor = conn.cursor()

    query = """SELECT year, COUNT(year) AS count
            FROM analysis_movies
            GROUP BY year
            """
    df = pd.read_sql(query, conn)

    fig = create_figure(df)

    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/graph')
def graph():
    return render_template("hello.html", Test="Channing!")


if __name__ == '__main__':
    app.run(debug=True)
