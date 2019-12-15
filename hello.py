# import libraries
import io
import pandas as pd
from flask import Flask, render_template, Response
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap
from graph import create_figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from sql import configuration, sqldb_conn, fetch_query, write_to_sql

# Create an instance of the Flask class
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

# Homepage of the web app
@app.route('/')
def index():
    return render_template('home.html', name='Channing!')

# Hello page to plot the graph using the result of a SQL query
@app.route('/plot.png')
def plot():
    """ SQL query and plot graph

    Connect to the Azure SQL Database and making a query.
    Then use the query result to plot a graph.
    This graph will be used by the hello.html.
    """

    # Connect to the Azure SQL database
    driver, server, db, uid, pwd = configuration()
    conn, cursor = sqldb_conn(driver, server, db, uid, pwd)
    
    # Making the SQL query
    query = fetch_query()

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
    """ Define the list of fields in the form
    """

    # 3 compulsory input fields in the form
    user_id = IntegerField('User ID', validators=[InputRequired()])
    movie_id = IntegerField('Movie ID', validators=[InputRequired()])
    comment = StringField('Tell me how you feel about this movie', validators=[InputRequired()])
    # Submit button in the form
    submit = SubmitField('Submit')

# Comment page that lets users to input their movie comments
@app.route('/comment', methods=['GET', 'POST'])
def comment():

    """ Get movie comments and input to the database

    Get users' movie comments as inputs.
    Then insert these inputs into the comments database.
    """

    # Declare input variables
    user_id = None
    movie_id = None
    comment = None

    # Create a form instance
    form = NameForm()

    # Check inputs validity
    if form.validate_on_submit():
        user_id = form.user_id.data
        movie_id = form.movie_id.data
        comment = form.comment.data
        # Insert inputs into comments database
        write_to_sql(user_id, movie_id, comment)
        # Clear form entries
        form = NameForm(formdata=None)
    return render_template('comment.html', form=form, user_id=user_id, \
                            movie_id=movie_id, comment=comment, name='Channing!')


if __name__ == '__main__':
    app.run(debug=True)