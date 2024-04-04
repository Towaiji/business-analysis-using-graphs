"""CSC111 Project 2

This module contains functions that run through the data files
to clean them based on completeness and reliability
and filter them according to certain criteria chosen by the user


Copyright and Usage Information
===============================

This file is provided solely for the personal and private use for Ali Towaiji and Tanay langhe.
All forms of distribution of this code, whether as given or with any changes, are expressly prohibited.

This file is Copyright (c) 2024 Ali Towaiji and Tanay Langhe
"""
import json


def parse(path: list) -> list:
    """
    Command used to recieve file and output its data

    Preconditions:
            - all inputs are valid American state names or test
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


def get_states() -> list:
    """
    Command used to get the desired American states from the user

    Preconditions:
            - all inputs are non-empty strings
    """
    states = input("Enter desired states followed by a comma (Ex. Alabama, Texas): ").split(",")
    clean_states = []
    for state in states:
        clean_states.append(state.strip().replace(" ", "_"))

    state_files = []
    for file in clean_states:
        state_files.append("meta-" + file + ".json")

    return state_files


def get_criteria():
    """
    Command used to get the criteria needed from the user
    """
    print("Please enter the criteria for the business you are searching for:")
    min_rating = float(input("Minimum average rating (1-5): "))
    min_reviews = int(input("Minimum number of reviews: "))
    category = input("Category (leave blank if no preference): ").strip()

    return min_rating, min_reviews, category
