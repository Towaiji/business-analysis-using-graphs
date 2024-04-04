"""
Main operations
"""
import pandas as pd

from Data_Loader import parse, filter_data, get_criteria, find_similar_businesses
from Graph_Opertations import Graph, _Vertex
from visualization import visualize_graph
import plotly.express as px


def visualize_businesses_on_map(businesses):
    df = pd.DataFrame([{
        'name': b[0], 'latitude': b[2], 'longitude': b[3], 'score': b[1]
    } for b in businesses])

    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="name",
                            color="score", size="score",
                            color_continuous_scale=px.colors.cyclical.IceFire, size_max=15,
                            zoom=10, mapbox_style="carto-positron")
    fig.show()


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
    print(similar_businesses)
    # Step 4: Visualize the similar businesses
    if similar_businesses:
        print(f"Found {len(similar_businesses)} similar businesses. Visualizing now...")
        visualize_businesses_on_map(similar_businesses)
    else:
        print("No similar businesses found based on the criteria.")


if __name__ == "__main__":
    main()
