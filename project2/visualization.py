import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json


def visualize_from_json(json_file_path, plot_type, x_column, y_column=None):
    """
    Visualizes data from a JSON file using seaborn.

    :param json_file_path: Path to the JSON file containing the data.
    :param plot_type: Type of plot to create ('boxplot' or 'barplot').
    :param x_column: The column to be used on the x-axis.
    :param y_column: The column to be used on the y-axis (optional for certain plots).
    """
    # Load data
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Convert data to DataFrame
    df = pd.DataFrame(data)

    # Create plot
    plt.figure(figsize=(10, 6))

    if plot_type == 'boxplot':
        sns.boxplot(data=df, x=x_column, y=y_column)
    elif plot_type == 'barplot':
        sns.barplot(data=df, x=x_column, y=y_column)
    else:
        print(f"Plot type '{plot_type}' is not supported.")
        return

    # Display plot
    plt.title(f'{plot_type.capitalize()} of {y_column} Across {x_column}')
    plt.ylabel(y_column if y_column else 'Value')
    plt.xlabel(x_column)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


#visualize_from_json('path/to/your_file.json', 'boxplot', 'category', 'avg_rating')
