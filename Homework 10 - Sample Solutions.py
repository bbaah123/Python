# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 01:13:27 2024

@author: USER
"""

import csv
import pandas as pd
import json

# Problem 1: Modify Existing CSV File
def modify_csv():
    df = pd.read_csv('example.csv')
    df['Email'] = ['john@example.com', 'jane@example.com']
    df.to_csv('updated_example.csv', index=False)

# Problem 2: Filter and Save Specific Data
def filter_csv():
    df = pd.read_csv('pandas_example.csv')
    filtered_df = df[df['Age'] > 25]
    filtered_df.to_csv('age_filtered.csv', index=False)

# Problem 3: Merge Two CSV Files
def merge_csv():
    df1 = pd.read_csv('example.csv')
    df2 = pd.read_csv('additional_data.csv')
    merged_df = pd.merge(df1, df2, on='SN')
    merged_df.to_csv('merged_data.csv', index=False)

# Problem 4: CSV to JSON Converter
def csv_to_json():
    df = pd.read_csv('pandas_example.csv')
    df.to_json('data.json', orient='records', indent=4)

# Problem 5: Handling Custom Delimiter
def read_custom_delimiter():
    with open('custom_delimiter.csv', 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            print(row)

# Problem 6: Update JSON File
def update_json():
    with open('data.json', 'r') as file:
        data = json.load(file)
    data['occupation'] = 'Engineer'
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

# Problem 7: JSON to CSV Converter
def json_to_csv():
    with open('data.json', 'r') as file:
        data = json.load(file)
    df = pd.DataFrame(data)
    df.to_csv('data_from_json.csv', index=False)

# Problem 8: Filtering JSON Data
def filter_json():
    with open('data.json', 'r') as file:
        data = json.load(file)
    filtered_data = [d for d in data if d.get('hasChildren')]
    print(filtered_data)

# Problem 9: Complex JSON Structure
def complex_json_structure():
    complex_data = [
        {"id": 1, "details": {"name": "John", "hobbies": ["Reading", "Cycling"]}},
        {"id": 2, "details": {"name": "Jane", "hobbies": ["Photography", "Traveling"]}}
    ]
    with open('complex_data.json', 'w') as file:
        json.dump(complex_data, file, indent=4)

# Problem 10: Custom Object to JSON
class User:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

def encode_user(o):
    if isinstance(o, User):
        return {'name': o.name, 'age': o.age, 'hobbies': o.hobbies, o.__class__.__name__: True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

def custom_object_to_json():
    user = User("John Doe", 30, ["Tennis", "Golf"])
    userJSON = json.dumps(user, default=encode_user, indent=4)
    print(userJSON)

# Execute functions to test
modify_csv()
filter_csv()
merge_csv()
csv_to_json()
read_custom_delimiter()
update_json()
json_to_csv()
filter_json()
complex_json_structure()
custom_object_to_json()
