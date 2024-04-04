import pandas as pd
import plotly.express as px

def visualize_businesses_on_map(graph):
    # Make sure the scores are already computed in the graph
    graph.compute_scores()  # figure out proper score system

    # Extract data for DataFrame
    # Convert the vertex data (including the score) into a format suitable for creating a DataFrame
    data = [{
        'name': vertex['name'],
        'latitude': vertex['latitude'],
        'longitude': vertex['longitude'],
        'score': vertex['score']  # Score as computed by compute_scores
    } for vertex in graph.get_vertices_data()]

    df = pd.DataFrame(data)

    # Generate the map
    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="name",
                            color="score", size="score",
                            color_continuous_scale=px.colors.cyclical.IceFire, size_max=15,
                            zoom=10, mapbox_style="carto-positron")
    fig.show()
