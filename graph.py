# Import libraries
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def create_figure(df):
    """ Create graph method
    """
    # Set figure size
    fig = Figure(figsize=(9,6))
    # Set x range
    x = range(len(df))
    # Set x & y lables
    axis = fig.add_subplot(1,1,1, xlabel='Year', ylabel='Number of films')
    # Set graph title
    axis.set_title('Number of films in the ranking each year', size=22)
    # Define correct tick labels for the x-axis
    x = df['year']
    # Assign x-axis' tick labels and font size
    axis.tick_params(axis='x', labelsize=10)
    # Rotate x-axis' tick labels
    plt.setp(axis.xaxis.get_majorticklabels(), rotation='vertical')
    # Plot the bar chart
    axis.bar(x, height=df['count'])
    return fig