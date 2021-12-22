import json


def generate_diff(first_file, second_file):
    with open(first_file) as f1:
        with open(second_file) as f2:
            first_file = json.load(f1)
            second_file = json.load(f2)
            return get_diff(first_file, second_file)


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


def get_diff(first, second=None):

    if not isinstance(first, dict):
        return first

    if second is None:
        second = first

    all_keys = get_keys(first, second)['all']
    removed_keys = get_keys(first, second)['removed']
    added_keys = get_keys(first, second)['added']
    kept_keys = get_keys(first, second)['kept']

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
                    'new value': get_diff(second[key])
                }

            else:
                result_diff[key] = {
                    'state': 'nested',
                    'value': get_diff(first[key], second[key]),
                }
    return result_diff  # in format { key: {state, value / old_value, new_value} }


first_file = r'../../tests/fixtures/json/file3.json'
second_file = r'../../tests/fixtures/json/file4.json'

print(generate_diff(first_file, second_file))



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

