"""
Main operations
"""
from Data_Loader import get_criteria, find_similar_businesses
from visualization import visualize_businesses_on_map
from Graph_Opertations import Graph, _Vertex


def main():
    """
    main function responsible for running all files
    """
    # g = Graph()
    # g.create_graph(data)
    # visualize_graph(g, ['rating', 'rev_num', 'category', 'loc'])
    #
    database = ['test.json']  # Your loaded dataset of businesses

    # Step 2: Get user-defined criteria
    min_rating, min_reviews, category = get_criteria()

    # Step 3: Find similar businesses based on criteria
    similar_businesses = find_similar_businesses(database, min_rating, min_reviews, category)

    # Step 4: Visualize the similar businesses
    if similar_businesses:
        print(f"Found {len(similar_businesses)} similar businesses. Visualizing now...")
        visualize_businesses_on_map(similar_businesses)
    else:
        print("No similar businesses found based on the criteria.")


if __name__ == "__main__":
    main()

#[[]]
