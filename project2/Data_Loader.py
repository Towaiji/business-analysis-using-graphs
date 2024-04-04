"""
This document is used to load the data from the file into readable and usable data
"""
import json


def parse(path: list):
    """
    Command used to recieve file and output its data
    """
    data = []
    for f in path:
        with open(f) as file:
            for l in file:
                dic = json.loads(l)
                req_keys = ['name', 'address', 'longitude', 'latitude', 'category', 'avg_rating', 'num_of_reviews', 'hours']
                if 'state' in dic.keys() and all(key in dic.keys() for key in req_keys):
                    if dic['state'] != "Permanently closed" and all(dic[key] is not None for key in req_keys):
                        dic.pop('gmap_id')
                        dic.pop('MISC')
                        dic.pop('relative_results')
                        dic.pop('url')
                        dic.pop('description')
                        dic.pop('price')
                        entry = list(dic.values())
                        data.append(entry)
        return data


def get_user_input(prompt, default_value):
    """Helper function to get user input with a default value."""
    user_input = input(prompt + f" (default {default_value}): ").strip()
    return float(user_input) if user_input else default_value


def filter_data(data):
    """Filter the data based on user inputs for various criteria."""
    min_rating = get_user_input("Enter minimum rating", 0)
    min_reviews = get_user_input("Enter minimum number of reviews", 0)
    desired_category = input("Enter desired category (leave blank if no preference): ").strip()
    desired_day = input("Enter a day to check if open (e.g., 'Monday'; leave blank if no preference): ").strip().capitalize()
    filtered_data = []
    for business in data:
        category_match = desired_category.lower() in [cat.lower() for cat in business[4]] if desired_category else True
        day_match = any(day.lower() == desired_day.lower() for day, hours in business[7]) if desired_day else True

        if business[5] >= min_rating and business[6] >= min_reviews and category_match and day_match:
            filtered_data.append(business)

    return filtered_data




#####################################

def get_criteria():
    print("Please enter the criteria for the business you are searching for:")
    min_rating = float(input("Minimum average rating (1-5): "))
    min_reviews = int(input("Minimum number of reviews: "))
    category = input("Category (leave blank if no preference): ").strip()

    # You can extend this with more criteria as needed
    return min_rating, min_reviews, category


def find_similar_businesses(database, min_rating, min_reviews, category):
    similar_businesses = []
    parsed_data = parse(database)
    for business in parsed_data:
        score = 0
        if float(business[5]) >= min_rating:
            score += 1
        if float(business[6]) >= min_reviews:
            score += 1
        if not category or category.lower() in [c.lower() for c in business[4]]:
            score += 1

        # You can adjust the scoring system as needed
        if score > 0:  # This means the business matches at least one criterion
            similar_businesses.append((business, score))

    # Sort businesses by their score for best matches
    similar_businesses.sort(key=lambda x: x[1], reverse=True)
    return similar_businesses
