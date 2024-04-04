"""CSC111 Project 2

This module contains the main operations function which runs the whole program using the other modules:
Data_loader.py
Graph_operations.py
Visualization.py


Copyright and Usage Information
===============================

This file is provided solely for the personal and private use for Ali Towaiji and Tanay langhe.
All forms of distribution of this code, whether as given or with any changes, are expressly prohibited.

This file is Copyright (c) 2024 Ali Towaiji and Tanay Langhe
"""
import python_ta
from Data_Loader import get_criteria, parse, get_states
from visualization import visualize_businesses_on_map
from Graph_Opertations import Graph


def main() -> None:
    """
    Main function responsible for running all files
    """
    g = Graph()
    database = get_states()  # loaded dataset of businesses
    parsed_data = parse(database)
    for entry in parsed_data:
        g.add_vertex(entry)

    # Get user-defined criteria
    min_rating, min_reviews, category = get_criteria()

    # filter the data using the criteria given
    g.filter_data(category, min_reviews, min_rating)

    # match businesses based similarity
    g.build_edges(category)

    # Visualize the similar businesses
    if g.get_vertices_data():
        print(f"Found {len(g.get_vertices_data())} similar businesses. Visualizing now...")
        visualize_businesses_on_map(g)
    else:
        print("No similar businesses found based on the criteria.")


if __name__ == "__main__":
    main()

    # python_ta.check_all(config={
    #     'extra-imports': [],  # the names (strs) of imported modules
    #     'allowed-io': [print(), input()],     # the names (strs) of functions that call print/open/input
    #     'max-line-length': 120
    # })
