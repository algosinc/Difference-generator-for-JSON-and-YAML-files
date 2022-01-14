import json
import yaml
from os import path
from gendiff.constants import *
from gendiff.scripts.formatters.stylish import stylish_formatter


def format_output(diff, formatter_style):
    if formatter_style == STYLISH:
        result = stylish_formatter(diff)
#        print(f'stylish_formatter: \n {result}')
        return result

    if formatter_style == PLAIN:
        return stylish_formatter(diff)

    if formatter_style == JSON:
        return stylish_formatter(diff)

    else:
        print(f'Wrong output format: {formatter_style}. Supported formats: {STYLISH}, {PLAIN}, {JSON}'.format)


def generate_diff(first_file, second_file, formatter_style):
    with open(first_file) as f1, open(second_file) as f2:
        _, file_type = path.splitext(first_file)

        if file_type == '.json':
            first = json.load(f1)
            second = json.load(f2)

        if file_type == '.yml' or file_type == '.yaml':
            first = yaml.safe_load(f1)
            second = yaml.safe_load(f2)

        result_diff = get_diff(first, second)
#        print(f'result_diff: \n {result_diff}')
        return format_output(result_diff, formatter_style)


def get_keys(first: dict, second: dict):
    """[summary]
        Args:
            dict1 ([type]): [description]
            dict2 ([type]): [description]
        Returns:
            [type]: [description]
    """
    keys_1 = set(first.keys())
    keys_2 = set(second.keys())
    keys = {}
    keys['all'] = sorted(list(keys_1 | keys_2))
    keys['added'] = list(keys_2 - keys_1)
    keys['removed'] = list(keys_1 - keys_2)
    keys['kept'] = list(keys_1 & keys_2)
    return keys


def get_diff(first, second=None):       # creating diff in intermediate format

    if not isinstance(first, dict):
        return first

    if second is None:
        second = first

    all_keys = get_keys(first, second)['all']
    removed_keys = get_keys(first, second)['removed']
    added_keys = get_keys(first, second)['added']
#    kept_keys = get_keys(first, second)['kept']

    result_diff = {}

    for key in all_keys:
        if key in added_keys:
            result_diff[key] = {
                'state': 'added',
                'value': get_diff(second[key])  # make recursion
            }

        elif key in removed_keys:
            result_diff[key] = {
                'state': 'removed',
                'value': get_diff(first[key])
            }

        else:
            if first[key] == second[key]:
                result_diff[key] = {
                    'state': 'unchanged',
                    'value': get_diff(first[key])
                }

            elif not isinstance(first[key], dict) or not isinstance(second[key], dict):
                result_diff[key] = {
                    'state': 'changed',
                    'value': get_diff(first[key]),
                    'new_value': get_diff(second[key])
                }

            else:
                result_diff[key] = {
                    'state': 'nested',
                    'value': get_diff(first[key], second[key]),
                }
    return result_diff  # in format { key: {state, value / old_value, new_value} }


'''
def generate_diff(first_file, second_file, formatter_style):
    with open(first_file) as f1, open(second_file) as f2:
        _, file_type = path.splitext(first_file)

        if file_type == '.json':
            first = json.load(f1)
            second = json.load(f2)

        if file_type == '.yml' or file_type == '.yaml':
            first = yaml.safe_load(f1)
            second = yaml.safe_load(f2)

        result_diff = get_diff(first, second)
        print(f'result_diff: \n {result_diff}')
        return format_output(result_diff, formatter_style)


def get_diff(first: dict, second: dict):
    result_diff = {}
    removed_keys = first.keys() - second.keys()
    added_keys = second.keys() - first.keys()
    saved_keys = first.keys() & second.keys()

    for key in saved_keys:
        first_val = first[key]
        second_val = second[key]

        if isinstance(first_val, dict) and isinstance(second_val, dict):  # if value is nested dict
            result_diff[key] = {
                STATE: NESTED,
                VALUE: get_diff(first_val, second_val) # make recursion
            }
        elif first_val == second_val:   # unchanged
            result_diff[key] = {
                STATE: UNCHANGED,
                VALUE: first_val
            }
        else:                           # changed
            result_diff[key] = {
                STATE: CHANGED,
                VALUE: first_val,
                NEW_VALUE: second_val
            }

    for key in removed_keys:
        result_diff[key] = {
            STATE: REMOVED,
            VALUE: first[key]
        }
    for key in added_keys:
        result_diff[key] = {
            STATE: ADDED,
            VALUE: second[key]
        }

    return result_diff  # in format { key: {state, value / old_value, new_value} }


# def get_diff(first: dict, second: dict):  # creating diff in intermediate format
#     result_diff = []                      # { key: {state, value, new_value} }
#     removed_keys = first.keys() - second.keys()
#     added_keys = second.keys() - first.keys()
#     saved_keys = first.keys() & second.keys()
#
#     for key in saved_keys:
#         first_val = first[key]
#         second_val = second[key]
#
#         if isinstance(first_val, dict) and isinstance(second_val, dict):  # if value is nested dict
#             result_diff.append({
#                 'key': key,
#                 STATE: NESTED,
#                 VALUE: get_diff(first_val, second_val)  # make recursion
#             })
#         elif first_val == second_val:   # unchanged
#             result_diff.append({
#                 'key': key,
#                 STATE: UNCHANGED,
#                 VALUE: first_val
#             })
#         else:                           # changed
#             result_diff.append({
#                 'key': key,
#                 STATE: 'changed',
#                 VALUE: first_val,
#                 'new value': second_val
#             })
#
#     for key in removed_keys:            # removed
#         result_diff.append({
#             'key': key,
#             STATE: 'removed',
#             VALUE: first[key]
#         })
#     for key in added_keys:              # added
#         result_diff.append({
#             'key': key,
#             STATE: 'added',
#             VALUE: second[key]
#         })
#     print(f'result_diff: \n {result_diff}')
#     return result_diff

'''
