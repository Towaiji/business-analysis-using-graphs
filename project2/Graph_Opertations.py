"""
This document is used to set up the groph class and its various function
"""
from __future__ import annotations
from typing import Any



class _Vertex:
    """A vertex in a graph.

    Instance Attributes:
        - item: The data stored in this vertex.
        - neighbours: The vertices that are adjacent to this vertex.
    """
    item: Any
    neighbours: set[_Vertex]

    def __init__(self, item: Any, neighbours: set[_Vertex]) -> None:
        """Initialize a new vertex with the given item and neighbours."""
        self.item = item
        self.neighbours = neighbours


class Graph:
    """A graph.
    #
    #     Representation Invariants:
    #     - all(item == self._vertices[item].item for item in self._vertices)
    #     # Private Instance Attributes:
    #     #     - _vertices: A collection of the vertices contained in this graph.
    #     #                  Maps item to _Vertex instance.
    """
    _vertices: dict[Any, _Vertex]

    def __init__(self):
        self._vertices = {}

    def get_vertices_data(self):
        """
        Public method to get data of all vertices in the graph.

        Returns:
            A list of dictionaries, each representing the data stored in a vertex.
        """
        return [vertex.item for vertex in self._vertices.values()]


    def add_vertex(self, item):
        if item['address'] not in self._vertices:
            self._vertices[item['address']] = _Vertex(item, set())

    def build_edges_based_on_criteria(self, category=None, rating_threshold=0.5, reviews_threshold=10):
        for vertex1 in self._vertices.values():
            for vertex2 in self._vertices.values():
                if vertex1 != vertex2 and self.is_similar(vertex1.item, vertex2.item, category, rating_threshold, reviews_threshold):
                    vertex1.neighbours.add(vertex2)
                    vertex2.neighbours.add(vertex1)

    def is_similar(self, item1, item2, category, rating_threshold, reviews_threshold):
        # Check for category match if a category is specified
        if category:
            categories1 = set([c.lower() for c in item1.get('category', [])])
            categories2 = set([c.lower() for c in item2.get('category', [])])
            if not categories1 & categories2:  # If there's no intersection in categories, they're not considered similar
                return False

        # Check if the average rating difference is within the threshold
        if abs(item1.get('avg_rating', 0) - item2.get('avg_rating', 0)) > rating_threshold:
            return False

        # Check if the number of reviews difference is within the threshold
        if abs(item1.get('num_of_reviews', 0) - item2.get('num_of_reviews', 0)) > reviews_threshold:
            return False

        return True

    #THIS NEEDS TO BE CHANGED TO AN ACTUAL SCORE CALCULATION
    def compute_scores(self):
        for vertex in self._vertices.values():
            vertex.item['score'] = len(vertex.neighbours)
