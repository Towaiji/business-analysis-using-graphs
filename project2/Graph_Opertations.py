"""CSC111 Project 2

This module contains the graph operations functions,
every function that creates a graph, adds vertices and edges between them will be here.
Also, there are functions for computing scores and finding if vertices are similar


Copyright and Usage Information
===============================

This file is provided solely for the personal and private use for Ali Towaiji and Tanay langhe.
All forms of distribution of this code, whether as given or with any changes, are expressly prohibited.

This file is Copyright (c) 2024 Ali Towaiji and Tanay Langhe
"""
from __future__ import annotations
from typing import Any
import python_ta


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

    def get_vertices_data(self) -> list:
        """
        Public method to get data of all vertices in the graph.

        Returns:
            A list of dictionaries, each representing the data stored in a vertex.
        """
        return [vertex.item for vertex in self._vertices.values()]

    def add_vertex(self, item: dict) -> None:
        """
        Function used to add vertices to a graph, adds them with their given address
        """
        if item['address'] not in self._vertices:
            self._vertices[item['address']] = _Vertex(item, set())

    def filter_data(self, category: str, min_rev: float | int, min_rating: float | int) -> None:
        """
        Function used to filter the data based on a certain category, minimum rating and review number
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

    def build_edges(self, category=None) -> None:
        """
        Builds edges using a helper function based on relations
        """
        for vertex1 in self._vertices.values():
            for vertex2 in self._vertices.values():
                if vertex1 != vertex2 and self.is_similar(vertex1.item, vertex2.item, category):
                    vertex1.neighbours.add(vertex2)
                    vertex2.neighbours.add(vertex1)

    def is_similar(self, item1: dict, item2: dict, category) -> bool:
        """
        Checks if 2 vertices are similar in order to see if they satisfy the condition to add an edge between them.
        They must be within a certain rating threshold a reviews threshold and if a category is specified then
        they must share a category
        """
        rating_threshold = 0.5
        reviews_threshold = 10
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

    def compute_scores(self) -> None:
        """
        Finds the score of each vertex based on calculation that relates to all filtered vertices
        it divides each vertex's rating by the maximum rating and the same with the review numbers and multiplies them
        by chosen constants and also finds its degree and devides it by the amount of vertices in the graph
        in order to calculate a score
        """
        # Constants to adjust the influence of each factor on the final score
        rating_weight = 1
        review_count_weight = 0.01
        connectivity_weight = 0.5

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
                                                               len(self._vertices) - 1)) * connectivity_weight

            # Calculate the final score by combining the factors
            vertex.item['score'] = round((rating_score + review_score + connectivity_score) * 6.5)


if __name__ == "__main__":

    python_ta.check_all(config={
        'extra-imports': [],  # the names (strs) of imported modules
        'allowed-io': [print(), input()],     # the names (strs) of functions that call print/open/input
        'max-line-length': 120
    })
