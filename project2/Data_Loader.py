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
                        data.append(dic)
        return data

#####################################

def get_criteria():
    print("Please enter the criteria for the business you are searching for:")
    min_rating = float(input("Minimum average rating (1-5): "))
    min_reviews = int(input("Minimum number of reviews: "))
    category = input("Category (leave blank if no preference): ").strip()

    # You can extend this with more criteria as needed
    return min_rating, min_reviews, category


def get_states():
    states = input("Enter desired states: ").strip()

    # You can extend this with more criteria as needed
    return states


# def find_similar_businesses(database, min_rating, min_reviews, category):
#     similar_businesses = []
#     parsed_data = parse(database)
#     for business in parsed_data:
#         score = 0
#         if float(business[5]) >= min_rating:
#             score += 1
#         if float(business[6]) >= min_reviews:
#             score += 1
#         if not category or category.lower() in [c.lower() for c in business[4]]:  # maybe require same category
#             score += 1
#
#         # You can adjust the scoring system as needed
#         if score > 0:  # This means the business matches at least one criterion
#             business.append(score)
#             similar_businesses.append(business)
#
#     # Sort businesses by their score for best matches
#     similar_businesses.sort(key=lambda x: x[1], reverse=True)
#
#     return similar_businesses
