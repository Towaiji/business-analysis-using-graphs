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
        """
        function used to add vertices to a graph,
        adds them with their given address
        """
        if item['address'] not in self._vertices:
            self._vertices[item['address']] = _Vertex(item, set())

    def filter_data(self, category, min_rev, min_rating):
        """
        :param category:
        :param min_rev:
        :param min_rating:
        :return:
        """
        remove_list = []
        cgry = set()
        cgry.add(category)
        for vertex in self._vertices:
            # print(set(self._vertices[vertex].item['category']))
            # print(cgry)
            if not((set(self._vertices[vertex].item['category']).intersection(cgry) or category == "") and
            self._vertices[vertex].item['avg_rating'] >= min_rating
            and self._vertices[vertex].item['num_of_reviews'] >= min_rev):
                remove_list.append(vertex)

        for removed in remove_list:
            self._vertices.pop(removed)





    def build_edges_based_on_criteria(self, category=None, rating_threshold=0.5, reviews_threshold=10):
        """
        builds edges using a helper function based on relations
        """
        for vertex1 in self._vertices.values():
            for vertex2 in self._vertices.values():
                if vertex1 != vertex2 and self.is_similar(vertex1.item, vertex2.item, category, rating_threshold,
                                                          reviews_threshold):
                    vertex1.neighbours.add(vertex2)
                    vertex2.neighbours.add(vertex1)

    def is_similar(self, item1, item2, category, rating_threshold, reviews_threshold):
        """
        checks if 2 vertices are similar
        in order to see if they satisfy the condition to add an edge between them
        """
        # Check for category match if a category is specified
        if category:
            categories1 = set([c.lower() for c in item1.get('category', [])])
            categories2 = set([c.lower() for c in item2.get('category', [])])
            if not categories1 & categories2:  # If there's no intersection in categories, they're not similar
                return False

        # Check if the average rating difference is within the threshold
        if abs(item1['avg_rating'] - item2['avg_rating']) > rating_threshold:
            return False

        # Check if the number of reviews difference is within the threshold
        if abs(item1['num_of_reviews'] - item2['num_of_reviews']) > reviews_threshold:
            return False

        return True

    def compute_scores(self):
        """
        finds the score of each vertex based on calculation that relates to all filtered vertices
        """
        # Constants to adjust the influence of each factor on the final score
        rating_weight = 1
        review_count_weight = 0.01  # Assuming review counts can be much larger than ratings
        connectivity_weight = 0.5  # Adjust based on how much you value connectivity

        # Normalize ratings and review counts to ensure fair comparison
        max_rating = max(
            vertex.item.get('avg_rating', 0) for vertex in self._vertices.values() if 'avg_rating' in vertex.item)
        max_reviews = max(vertex.item.get('num_of_reviews', 0) for vertex in self._vertices.values() if
                          'num_of_reviews' in vertex.item)

        for vertex in self._vertices.values():
            rating_score = (vertex.item.get('avg_rating', 0) / max_rating if max_rating else 0) * rating_weight
            review_score = (vertex.item.get('num_of_reviews',
                                            0) / max_reviews if max_reviews else 0) * review_count_weight
            connectivity_score = (len(vertex.neighbours) / max(1,
                                                               len(self._vertices) - 1)) * connectivity_weight  # Normalize by the total possible connections

            # Calculate the final score by combining the factors
            vertex.item['score'] = round((rating_score + review_score + connectivity_score) * 6.5)
