import json
import yaml
from os import path


def generate_diff(first_file, second_file, format):
    with open(first_file) as f1:
        with open(second_file) as f2:

            _, file_type = path.splitext(first_file)

            if file_type == '.json':
                first = json.load(f1)
                second = json.load(f2)

            if file_type == '.yml' or file_type == '.yaml':
                first = yaml.safe_load(f1)
                second = yaml.safe_load(f2)

            return get_diff(first, second)


def get_diff(first: dict, second: dict):
    result_diff = []
    removed_keys = first.keys() - second.keys()
    added_keys = second.keys() - first.keys()
    saved_keys = first.keys() & second.keys()

    for key in saved_keys:
        first_val = first[key]
        second_val = second[key]

        if isinstance(first_val, dict) and isinstance(second_val, dict): # if value is nested dict
            result_diff.append({
                'key': key,
                'state': 'nested',
                'value': get_diff(first_val, second_val) # make recursion
            })
        elif first_val == second_val:   # unchanged
            result_diff.append({
                'key': key,
                'state': 'unchanged',
                'value': first_val
            })
        else:                           # changed
            result_diff.append({
                'key': key,
                'state': 'changed',
                'value': first_val,
                'new value': second_val
            })

    for key in removed_keys:
        result_diff.append({
            'key': key,
            'state': 'removed',
            'value': first[key]
        })
    for key in added_keys:
        result_diff.append({
            'key': key,
            'state': 'added',
            'value': second[key]
        })

    return result_diff  # in format { key: {state, value / old_value, new_value} }

#def diff_sort(diff):

# def test():
#     first_file = r'../tests/fixtures/json/file3.json'
#     second_file = r'../tests/fixtures/json/file4.json'
#     print(generate_diff(first_file, second_file))
#
# test()

# def get_diff(first: dict, second: dict):
#     result_diff = {}
#     removed_keys = first.keys() - second.keys()
#     added_keys = second.keys() - first.keys()
#     saved_keys = first.keys() & second.keys()
#
#     for key in saved_keys:
#         first_val = first[key]
#         second_val = second[key]
#
#         if isinstance(first_val, dict) and isinstance(second_val, dict): # if value is nested dict
#             result_diff[key] = {
#                 'state': 'nested',
#                 'value': get_diff(first_val, second_val) # make recursion
#             }
#         elif first_val == second_val:   # unchanged
#             result_diff[key] = {
#                 'state': 'unchanged',
#                 'value': first_val
#             }
#         else:                           # changed
#             result_diff[key] = {
#                 'state': 'changed',
#                 'old value': first_val,
#                 'new value': second_val
#             }
#
#     for key in removed_keys:
#         result_diff[key] = {
#             'state': 'removed',
#             'value': first[key]
#         }
#     for key in added_keys:
#         result_diff[key] = {
#             'state': 'added',
#             'value': second[key]
#         }
#
#     return result_diff  # in format { key: {state, value / old_value, new_value} }
