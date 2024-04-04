"""
Main operations
"""
from Data_Loader import get_criteria, parse
from visualization import visualize_businesses_on_map
from Graph_Opertations import Graph, _Vertex


def main():
    """
    main function responsible for running all files
    """
    g = Graph()
    database = ['test.json']  # Your loaded dataset of businesses
    parsed_data = parse(database)
    for entry in parsed_data:
        g.add_vertex(entry)

    # Step 2: Get user-defined criteria
    min_rating, min_reviews, category = get_criteria()


    # Step 3: Find similar businesses based on criteria
    g.build_edges_based_on_criteria(category, min_rating, min_reviews)


    # Step 4: Visualize the similar businesses
    if g._vertices:
        print(f"Found {len(g._vertices)} similar businesses. Visualizing now...")
        visualize_businesses_on_map(g)
    else:
        print("No similar businesses found based on the criteria.")


if __name__ == "__main__":
    main()

#[[]]
