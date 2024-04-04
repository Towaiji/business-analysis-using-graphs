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

def get_states():
    states = input("Enter desired states followed by a comma (Ex. Alabama, Texas): ").split(",")
    clean_states = []
    for state in states:
        clean_states.append(state.strip().replace(" ", "_"))

    state_files = []
    for file in clean_states:
        state_files.append("meta-" + file + ".json")

    return state_files

def get_criteria():
    print("Please enter the criteria for the business you are searching for:")
    min_rating = float(input("Minimum average rating (1-5): "))
    min_reviews = int(input("Minimum number of reviews: "))
    category = input("Category (leave blank if no preference): ").strip()

    # You can extend this with more criteria as needed
    return min_rating, min_reviews, category
