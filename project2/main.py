"""CSC111 Project 2

This module contains the main operations function which runs the whole program using the other modules:
Data_loader.py
Graph_operations.py
Visualization.py


Copyright and Usage Information
===============================

This file is provided solely for the personal and private use for Ali Towaiji and Tanay langhe
and the CSC111 teaching team at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) 2024 Ali Towaiji and Tanay Langhe
"""
from Data_Loader import get_criteria, parse, get_states
from visualization import visualize_businesses_on_map
from Graph_Opertations import Graph


def main():
    """
    main function responsible for running all files
    """
    g = Graph()
    database = get_states()  # Your loaded dataset of businesses
    parsed_data = parse(database)
    for entry in parsed_data:
        g.add_vertex(entry)

    # Step 2: Get user-defined criteria
    min_rating, min_reviews, category = get_criteria()

    g.filter_data(category, min_reviews, min_rating)

    # Step 3: Find businesses that match criteria
    g.build_edges_based_on_criteria(category)

    # Step 5: Visualize the similar businesses

    # Step 4: Visualize the similar businesses

    if g.get_vertices_data():
        print(f"Found {len(g.get_vertices_data())} similar businesses. Visualizing now...")
        visualize_businesses_on_map(g)
    else:
        print("No similar businesses found based on the criteria.")


if __name__ == "__main__":
    main()
