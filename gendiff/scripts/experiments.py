import json
from os import path

first_file = r'../../tests/fixtures/json/file1.json'
second_file = r'../../tests/fixtures/json/file2.json'


def get_json_data(file):
    fixed_data = file.read()  # convert multiple json objects to one by add []
    return json.load(file)  # return converted to dict json data


def generate_diff(first_file, second_file, parse_format):
    with open(first_file) as f1, open(second_file) as f2:
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


print(generate_diff(first_file, second_file, 'stylish'))
# print(generate_diff(first_file, second_file))


'''
def json_compare(first_json, second_json):
    keys = set(first_json.keys())
    keys_list = list(keys.union(set(second_json.keys())))
    keys_list.sort()
    result = ['{', ]
    for key in keys_list:
        if (key in first_json) and (key in second_json):
            if first_json[key] == second_json[key]:             # no changes
                result.append(f'    {json_encode(key)}: {json_encode(first_json[key])}')
            if first_json[key] != second_json[key]:             # value changed
                result.append(f'  - {json_encode(key)}: {json_encode(first_json[key])}')
                result.append(f'  + {json_encode(key)}: {json_encode(second_json[key])}')
            continue
        if (key in first_json) and not (key in second_json):
            result.append(f'  - {json_encode(key)}: {json_encode(first_json[key])}')  # noqa # remove item
            continue
        else:
            result.append(f'  + {json_encode(key)}: {json_encode(second_json[key])}')  # noqa # new item
    result.append('}')
    return '\n'.join(result)
    
    
def get_diff(first: dict, second: dict):
    result_diff = {}
    removed_keys = first.keys() - second.keys()
    added_keys = second.keys() - first.keys()
    saved_keys = first.keys() & second.keys()

    for key in saved_keys:
        first_val = first[key]
        second_val = second[key]

        if isinstance(first_val, dict) and isinstance(second_val, dict): # if value is nested dict
            result_diff[key] = {
                'state': 'nested',
                'value': get_diff(first_val, second_val) # make recursion
            }
        elif first_val == second_val:   # unchanged
            result_diff[key] = {
                'state': 'unchanged',
                'value': first_val
            }
        else:                           # changed
            result_diff[key] = {
                'state': 'changed',
                'old value': first_val,
                'new value': second_val
            }

    for key in removed_keys:
        result_diff[key] = {
            'state': 'removed',
            'value': first[key]
        }
    for key in added_keys:
        result_diff[key] = {
            'state': 'added',
            'value': second[key]
        }

    return result_diff  # in format { key: {state, value / old_value, new_value} }    
    
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
'''

