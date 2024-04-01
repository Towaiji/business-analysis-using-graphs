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
    neighbours: dict[Any, _Vertex]

    def __init__(self, item: Any, neighbours: dict[Any, _Vertex]) -> None:
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
            v1 = self._vertices[item1]
            v2 = self._vertices[item2]

            # Add the new edge
            v1.neighbours[edge_type] = v1.neighbours[edge_type].append(v2)
            v2.neighbours.add(v1)
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
        if abs(vertex1[5] - vertex2[5]) <= rating_threshold:
            return False

            # Check for minimum number of reviews
        if vertex1['num_of_reviews'] < 5 or vertex2['num_of_reviews'] < 5:
            return False

            # Check if they share a category
        if not set(vertex1['category']).intersection(vertex2['category']):
            return False


    def create_graph(self, data):
        """

        :param data:
        """
        parsed_data = parse(data)
        for item in parsed_data:
            self.add_vertex(item)

        for vertex1 in self._vertices:
            for vertex2 in self._vertices:
                if vertex1 != vertex2:
                    self.should_add_edge(vertex1, vertex2)
