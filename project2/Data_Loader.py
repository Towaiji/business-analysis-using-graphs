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
                req_keys = ['longitude', 'latitude', 'category', 'avg_rating', 'num_of_reviews', 'hours']
                if 'state' in dic.keys() and all(key in dic.keys() for key in req_keys):
                    if dic['state'] != "Permanently closed" and all(dic[key] is not None for key in req_keys):
                        dic.pop('gmap_id')
                        dic.pop('MISC')
                        dic.pop('relative_results')
                        dic.pop('url')
                        dic.pop('description')
                        dic.pop('price')
                        data.append(dic)
        return data[0]


def filter(file):
    """

    :return:
    """
