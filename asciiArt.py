
from ascii_graph import Pyasciigraph

def ascii_hist(dataset):
    """Using ascii_graph library, this function
    produces a pretty command line histogram output.
    """
<<<<<<< HEAD
    graph = Pyasciigraph(line_length=80,min_graph_length=1,separator_length=2,multivalue=False,human_readable='None',graphsymbol='*')

    for line in graph.graph(label="Most Frequent", data = dataset):
        print(line)
=======
    graph = Pyasciigraph(line_length=80,min_graph_length=1,separator_length=2,multivalue=False,human_readable='None', graphsymbol='*')
    
    for line in graph.graph(label="Most Frequent", data = dataset):
    		print(line)
>>>>>>> 97f96bb35ebaf613c34a78ec5d96264706f631e2
