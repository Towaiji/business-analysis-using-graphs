import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.express as px

# def visualize_graph(graph, edge_types):
#     edge_type_colors = {
#         'rating': 'blue',
#         'rev_num': 'red',
#         'category': 'green',
#         'loc': 'purple'
#     }
#
#     # Create Plotly figure
#     fig = make_subplots()
#
#     node_trace = go.Scatter(x=[], y=[], hovertext=[], text=[], mode='markers+text', textposition="bottom center",
#                             hoverinfo="text", marker={'size': 10, 'color': 'LightSkyBlue'})
#
#     edge_traces = {edge_type: go.Scatter(x=[], y=[], line={'width': 2, 'color': edge_type_colors[edge_type]},
#                                          hoverinfo='none', mode='lines') for edge_type in edge_types}
#
#     for item, vertex in graph._vertices.items():
#         x, y = vertex.item[2], vertex.item[3]  # Assuming these are positions
#         node_trace['x'] += tuple([x])
#         node_trace['y'] += tuple([y])
#         node_trace['hovertext'] += tuple([vertex.item[0]])
#
#         for edge_type, neighbours in vertex.neighbours.items():
#             if edge_type in edge_types:
#                 for neighbour in neighbours:
#                     edge_trace = edge_traces[edge_type]
#                     edge_trace['x'] += tuple([x, neighbour.item[2], None])
#                     edge_trace['y'] += tuple([y, neighbour.item[3], None])
#
#     fig.add_trace(node_trace)
#     for edge_trace in edge_traces.values():
#         fig.add_trace(edge_trace)
#
#     fig.update_layout(showlegend=False, hovermode='closest',
#                       margin={'b': 0, 'l': 0, 'r': 0, 't': 0},
#                       xaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
#                       yaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False})
#
#     fig.show()

def visualize_businesses_on_map(businesses):
    df = pd.DataFrame([{
        'name': b[0], 'latitude': b[2], 'longitude': b[3], 'score': b[9]
    } for b in businesses])

    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="name",
                            color="score", size="score",
                            color_continuous_scale=px.colors.cyclical.IceFire, size_max=15,
                            zoom=10, mapbox_style="carto-positron")
    fig.show()
