import plotly

import plotly.graph_objects as go


def visualize_graph(graph):
    edge_x = []
    edge_y = []
    edge_color = []

    node_x = []
    node_y = []
    node_text = []

    color_map = {
        'rating': 'blue',
        'rev_num': 'red',
        'category': 'green',
        'location': 'purple'
    }

    # Iterate through vertices to gather node and edge data
    for item, vertex in graph._vertices.items():
        x, y = vertex.item['longitude'], vertex.item['latitude']
        node_x.append(x)
        node_y.append(y)
        node_text.append(vertex.item['name'])

        for edge_type, neighbours in vertex.neighbours.items():
            for neighbour in neighbours:
                nx, ny = neighbour.item['longitude'], neighbour.item['latitude']
                edge_x.extend([x, nx, None])  # Add 'None' to create discontinuous segments
                edge_y.extend([y, ny, None])
                edge_color.append(color_map[edge_type])

    # Create the scatter plot for edges
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color=edge_color),
        hoverinfo='none',
        mode='lines')

    # Create the scatter plot for nodes
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        hoverinfo='text',
        text=node_text,
        marker=dict(
            showscale=False,
            color='black',
            size=10,
            line_width=2))

    # Define the layout
    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=20, l=5, r=5, t=40),
                        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                    )

    fig.show()
