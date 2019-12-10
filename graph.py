from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def create_figure(df):

    fig = Figure(figsize=(9,6))
    x = range(len(df))
    axis = fig.add_subplot(1,1,1, xlabel='Year', ylabel='Number of films')
    axis.set_title('Number of films in the ranking each year', size=22)
    x = df['year']
    axis.tick_params(axis='x', labelsize=10)
    plt.setp(axis.xaxis.get_majorticklabels(), rotation='vertical')
    axis.bar(x, height=df['count'])
    return fig