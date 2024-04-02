"""
This document is used to set up the groph class and its various function
"""
from __future__ import annotations
from typing import Any
from Data_Loader import parse


class _Vertex:
    """A vertex in a graph.

    Instance Attributes:
        - item: The data stored in this vertex.
        - neighbours: The vertices that are adjacent to this vertex.
    """
    item: Any
    neighbours: dict[Any, set[_Vertex]]

    def __init__(self, item: Any, neighbours: dict[Any, set[_Vertex]]) -> None:
        """Initialize a new vertex with the given item and neighbours."""
        self.item = item
        self.neighbours = neighbours


class Graph:
    """A graph.

    Representation Invariants:
    - all(item == self._vertices[item].item for item in self._vertices)
    """
    # Private Instance Attributes:
    #     - _vertices: A collection of the vertices contained in this graph.
    #                  Maps item to _Vertex instance.
    _vertices: dict[Any, _Vertex]

    def __init__(self) -> None:
        """Initialize an empty graph (no vertices or edges)."""
        self._vertices = {}

    def add_vertex(self, item: Any) -> None:
        """Add a vertex with the given item to this graph.

        The new vertex is not adjacent to any other vertices.

        Preconditions:
            - item not in self._vertices
        """
        self._vertices[item] = _Vertex(item, {})

    def add_edge(self, item1: Any, item2: Any, edge_type: Any) -> None:
        """Add an edge between the two vertices with the given items in this graph.

        Raise a ValueError if item1 or item2 do not appear as vertices in this graph.

        Preconditions:
            - item1 != item2
        """
        if item1 in self._vertices and item2 in self._vertices:
            self._vertices[item1].neighbours[edge_type].add(self._vertices[item2])
            self._vertices[item2].neighbours[edge_type].add(self._vertices[item1])

        else:
            # We didn't find an existing vertex for both items.
            raise ValueError

    def adjacent(self, item1: Any, item2: Any) -> bool:
        """Return whether item1 and item2 are adjacent vertices in this graph.

        Return False if item1 or item2 do not appear as vertices in this graph.
        """
        if item1 in self._vertices and item2 in self._vertices:
            v1 = self._vertices[item1]
            return any(v2.item == item2 for v2 in v1.neighbours)
        else:
            # We didn't find an existing vertex for both items.
            return False

    def get_neighbours(self, item: Any) -> set:
        """Return a set of the neighbours of the given item.

        Note that the *items* are returned, not the _Vertex objects themselves.

        Raise a ValueError if item does not appear as a vertex in this graph.
        """
        if item in self._vertices:
            v = self._vertices[item]
            return {neighbour.item for neighbour in v.neighbours}
        else:
            raise ValueError

    def should_add_edge(self, vertex1, vertex2):
        """
        return if should add adge
        """
        if abs(vertex1[5] - vertex2[5]) <= 0.5:
            self.add_edge(vertex1, vertex2, 'rating')

            # Check for minimum number of reviews
        if vertex1[6] - vertex2[6] <= 10:
            self.add_edge(vertex1, vertex2, 'rev_num')

            # Check if they share a category
        if set(vertex1[4]).intersection(set(vertex2[4])):
            self.add_edge(vertex1, vertex2, 'category')

        if abs(vertex1[3] - vertex2[3]) <= 10 and abs(vertex1[4] - vertex2[4]) <= 10:
            self.add_edge(vertex1, vertex2, 'location')

    def create_graph(self, data):
        """
        :param data:
        """
        parsed_data = parse(data)
        for item in parsed_data:
            self.add_vertex(item)

        visited = []
        for vertex1 in self._vertices:
            visited.append(vertex1)
            for vertex2 in self._vertices:
                if vertex1 != vertex2 and vertex2 not in visited:
                    self.should_add_edge(vertex1, vertex2)
