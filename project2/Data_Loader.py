"""
ADD MORE (CHECK PROJECT 2 WEBSITE CLEAR REQUIREMENTS ARE STATED)
This document is used to load the data from the file into readable and usable data
"""
import json


def parse(path: list):
    """
    MAKE REQUIREMENT THAT ALL VALUES IN PATH ARE VALID FILES
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

    # You can extend this with more criteria as needed
    return min_rating, min_reviews, category



def append_first_200_lines_to_existing_file(input_json_file_path):
    """
    Append the first 200 lines of a JSON file to an existing file named meta-test.json.
    If meta-test.json does not exist, it will be created.

    Parameters:
    - input_json_file_path: str, the path to the input JSON file.
    """
    try:
        with open(input_json_file_path, 'r') as input_file, open('meta-test.json', 'a') as output_file:
            # Optionally, add a separator if appending to an existing file for better readability or JSON structure
            output_file.write('\n')  # Ensure we start on a new line
            for i in range(200):
                line = input_file.readline()
                if not line:  # If the file has less than 200 lines
                    break
                output_file.write(line)
    except FileNotFoundError:
        print("The input file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# Replace 'path/to/your/input_json_file.json' with the actual path to your input JSON file.
# append_first_200_lines_to_existing_file('path/to/your/input_json_file.json')
