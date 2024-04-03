"""
Main operations
"""
from Data_Loader import parse, filter_data
from Graph_Opertations import Graph, _Vertex
from visualization import visualize_graph


def main(data):
    """
    main function responsible for running all files
    """
    g = Graph()
    g.create_graph(data)
    visualize_graph(g)
