# Project-2
This is the CSC111 project 2 done by Ali Towaiji and Tanay Langhe

Business Analysis Using Geospatial and Review Data
Overview
This project aims to analyze the success of businesses based on geospatial and review data. By setting specific criteria, users can filter businesses and visualize them on an interactive map with a scoring system to determine which businesses meet the user's criteria. The project leverages Python for data manipulation, Plotly for data visualization, and utilizes JSON files for business data across various states in the United States.

Key Features
User-Defined Criteria: Allows users to set criteria based on business ratings, reviews, and categories.

Geospatial Visualization: Visualizes the businesses on an interactive map with color-coded nodes indicating business success based on the criteria.

Scoring System: Computes scores for businesses based on their similarity to user-defined criteria.

Data Filtering and Parsing: Clean and filter business data based on user input to show relevant businesses.

How to Use
Prepare Data Files: You will need the meta-test.json and meta-test2.json data files for testing. You can use these files by placing them in the project directory.

Run the Program:

Upon running the program, you will be prompted to input the states you wish to check. You can use test or test2 for controlled testing with the provided data files.

Enter a minimum rating (1-5) and the minimum number of reviews.

Specify a business category (e.g., "Convenience store" or "Gas station").

The program will filter businesses that match your criteria and display them on a map with scoring nodes.

Visualization: After inputting the criteria, the businesses matching your filters will be displayed on a Mapbox map, with each business represented as a colored node based on its score.

Datasets
This project utilizes the Google Local Reviews dataset (2021), which includes business attributes like names, addresses, categories, ratings, Google Maps ID, price, hours, and reviews. The data is cleaned and filtered for accuracy, removing incomplete or unreliable entries.

Test Files: meta-test.json, meta-test2.json

Data Characteristics: Each entry includes the business's location, ratings, review counts, and category.

Computational Overview
The main components of the program are:

parse: Cleans the dataset, removing unnecessary data and keeping relevant information for analysis.

get_criteria: Prompts users to define business criteria (e.g., minimum rating, review count).

get_states: Asks users to select states for data analysis.

Graph Construction: Businesses are treated as vertices, and relationships between them (e.g., ratings, location) form edges.

Helper Functions:

add_vertex: Adds business locations as vertices.

build_edges: Constructs edges based on criteria similarity.

is_similar: Compares businesses to determine their similarity based on user input.

compute_scores: Calculates a business score based on similarity.

filter_data: Filters data by the user's criteria (category, rating, etc.).

Project Evolution
The project evolved from a simple data analysis into an interactive system where users can input custom criteria and visualize results on a map. Feedback from the proposal phase pushed us to enhance the complexity, incorporating interactive features like dynamic map visualizations and customizable filters for user-specific business insights.

Future Directions
Expanded Datasets: Integrating additional datasets for more comprehensive business analysis.

More Visualization Techniques: Introducing different graph types and analytical models to offer deeper insights.

Enhanced User Interaction: Making the interface more interactive and user-friendly.

Conclusion
This project demonstrates the power of data analysis, geospatial mapping, and computational techniques in understanding and predicting business success. It provides a valuable tool for users seeking to identify businesses that match specific criteria, enabling informed decision-making.

References
Li, Jiacheng, et al. "UCTopic: Unsupervised Contrastive Learning for Phrase Representations and Topic Mining." 2022.

Yan, An, et al. "Personalized Showcases: Generating Multi-Modal Explanations for Recommendations."
