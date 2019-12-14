# import libraries
import io
import pandas as pd
import pyodbc
from flask import Flask, render_template, Response
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap
from graph import create_figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from comment import write_sql

# Create an instance of the Flask class
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

# Homepage of the web app
@app.route('/')
def index():
    return render_template('home.html', name='Channing!')

# Hello page to show the graph using the result of a SQL query
@app.route('/plot.png')
def plot():
    """ SQL query and plot graph

    Using the connect function of pyodbc to connect to 
    the Azure SQL Database and
    making a query.

    Then using the query result to plot a graph.
    This graph will be used by the hello.html.
    """

    # Connect to the Azure SQL database
    conn = pyodbc.connect(
        'Driver={ODBC Driver 17 for SQL Server};'
        'Server=azuresqlorange.database.windows.net;'
        'Database=orange_azure;'
        'Trusted_Connectoin=yes;'
        'UID=orange;'
        'PWD=Supermotdepasse!42;')
    cursor = conn.cursor()

    # Making the SQL query
    query = """SELECT year, COUNT(year) AS count
            FROM analysis_movies
            GROUP BY year
            """
    # Putting the result in a dataframe
    df = pd.read_sql(query, conn)

    # Call the create_figure method from graph.py to plot a graph
    fig = create_figure(df)

    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

# Hello page to show the graph using the result of a SQL query
@app.route('/graph')
def graph():
    return render_template("hello.html", Test="Channing!")

class NameForm(FlaskForm):
    user_id = IntegerField('User ID', validators=[InputRequired()])
    movie_id = IntegerField('Movie ID', validators=[InputRequired()])
    comment = StringField('Tell me how you feel about this movie', validators=[InputRequired()])
    submit = SubmitField('Submit')


@app.route('/comment', methods=['GET', 'POST'])
def comment():
    user_id = None
    movie_id = None
    comment = None
    form = NameForm()
    if form.validate_on_submit():
        user_id = form.user_id.data
        movie_id = form.movie_id.data
        comment = form.comment.data
        write_sql(user_id, movie_id, comment)
        form = NameForm(formdata=None)
        movie_id = form.movie_id.data
    return render_template('comment.html', form=form, user_id=user_id, movie_id=movie_id, comment=comment, name='Channing!')


if __name__ == '__main__':
    app.run(debug=True)