def stylish_formatter(diff: dict):
    indent = '   '

# def diff_sort(diff):


# def json_compare(first_json, second_json):
#     keys = set(first_json.keys())
#     keys_list = list(keys.union(set(second_json.keys())))
#     keys_list.sort()
#     result = ['{', ]
#     for key in keys_list:
#         if (key in first_json) and (key in second_json):
#             if first_json[key] == second_json[key]:             # no changes
#                 result.append(f'    {json_encode(key)}: {json_encode(first_json[key])}')
#             if first_json[key] != second_json[key]:             # value changed
#                 result.append(f'  - {json_encode(key)}: {json_encode(first_json[key])}')
#                 result.append(f'  + {json_encode(key)}: {json_encode(second_json[key])}')
#             continue
#         if (key in first_json) and not (key in second_json):
#             result.append(f'  - {json_encode(key)}: {json_encode(first_json[key])}')  # noqa # remove item
#             continue
#         else:
#             result.append(f'  + {json_encode(key)}: {json_encode(second_json[key])}')  # noqa # new item
#     result.append('}')
#     return '\n'.join(result)
#
#
# def yaml_compare(first_yaml, second_yaml):
#     keys = set(first_yaml.keys())
#     keys_list = list(keys.union(set(second_yaml.keys())))
#     keys_list.sort()
#     result = []
#     for key in keys_list:
#         if (key in first_yaml) and (key in second_yaml):
#             if first_yaml[key] == second_yaml[key]:             # no changes
#                 result.append(f'  {yaml_encode(key)}: {yaml_encode(first_yaml[key])}')
#             if first_yaml[key] != second_yaml[key]:             # value changed
#                 result.append(f'- {yaml_encode(key)}: {yaml_encode(first_yaml[key])}')
#                 result.append(f'+ {yaml_encode(key)}: {yaml_encode(second_yaml[key])}')
#             continue
#         if (key in first_yaml) and not (key in second_yaml):
#             result.append(f'- {yaml_encode(key)}: {yaml_encode(first_yaml[key])}')  # remove item
#             continue
#         else:
#             result.append(f'+ {yaml_encode(key)}: {yaml_encode(second_yaml[key])}')  # new item
#     return '\n'.join(result)
#
#
# def json_encode(value_in_json):
#     return json.JSONEncoder().encode(value_in_json)
#
#
# def yaml_encode(value_in_yaml):
#     return yaml.safe_dump(value_in_yaml)[:-5]

def ttest():
    test_list = \
        [{'key': 'common', 'state': 'nested', 'value':
            [
                {'key': 'setting3', 'state': 'changed', 'old value': True, 'new value': None},
                {'key': 'setting6', 'state': 'nested', 'value': [
                    {'key': 'key', 'state': 'unchanged', 'value': 'value'},
                    {'key': 'doge', 'state': 'nested', 'value': [
                        {'key': 'wow', 'state': 'changed', 'old value': 'o', 'new value': 'so much'}
                    ]},
                    {'key': 'ops', 'state': 'added', 'value': 'vops'}]},
                {'key': 'setting1', 'state': 'unchanged', 'value': 'Value 1'},
                {'key': 'setting2', 'state': 'removed', 'value': 200},
                {'key': 'setting5', 'state': 'added', 'value':
                    {'key5': 'value5'}},
                {'key': 'setting4', 'state': 'added', 'value': 'blah blah'},
                {'key': 'follow', 'state': 'added', 'value': False}]},
            {'key': 'group1', 'state': 'nested', 'value':[
                {'key': 'baz', 'state': 'changed', 'old value': 'bas', 'new value': 'bars'},
                {'key': 'nest', 'state': 'changed', 'old value': {'key': 'value'}, 'new value': 'str'},
            {'key': 'foo', 'state': 'unchanged', 'value': 'bar'}]},
            {'key': 'group2', 'state': 'removed', 'value': {'abc': 12345, 'deep': {'id': 45}}},
            {'key': 'group3', 'state': 'added', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}
        ]


a = \
    [{'key': 'common', 'state': 'nested', 'value':
            [
                {'key': 'setting9', 'state': 'changed', 'value': True, 'new value': None},
                {'key': 'setting6', 'state': 'nested', 'value': 'vops'},
                {'key': 'setting4', 'state': 'unchanged', 'value': 'Value 1'},
                {'key': 'setting2', 'state': 'removed', 'value':
                    [
                    {'key': 'qwe2', 'state': 'removed', 'value': 12345},
                    {'key': 'asd', 'state': 'added', 'value': 'deep'}
                    ]
                }
            ]
      },
      {'key': 'group3', 'state': 'nested', 'value':[
            {'key': 'baz', 'state': 'changed', 'value': 'bas', 'new value': 'bars'},
            {'key': 'nest', 'state': 'changed', 'value': 'value123', 'new value': 'str'},
            {'key': 'foo', 'state': 'unchanged', 'value': 'bar'}
            ]
       },
      {'key': 'group2', 'state': 'removed', 'value': 12345},
      {'key': 'group1', 'state': 'added', 'value': 'deep'}
    ]

y = [
    {'key': 'setting9', 'state': 'changed', 'value': True, 'new value': None},
    {'key': 'setting6', 'state': 'nested', 'value': 'vops'},
    {'key': 'setting4', 'state': 'unchanged', 'value': 'Value 1'},
    {'key': 'setting2', 'state': 'removed', 'value':
        [
            {'key': 'qwe2', 'state': 'removed', 'value': 12345},
            {'key': 'asd', 'state': 'added', 'value': 'deep'}
        ]
    }
    ]


z = {"category": ["NONES","BACKEND"], "selector": "bus", "acrh": "isr", "priority": [4,3,1], "nl_date": "6/19/2005",
     "rl_date": "", "sl_date": "7/3/2040", "stats": {"zorts": 2, "busic": "", "ack": [54,34,21]}}

def for_sorting_data(data):
    sorted_data = []
    def sorting(d):
        for item in d:
            if isinstance(item['value'], list):
                sorting(item['value'])
        sort_result = sorted(item, key = lambda i: item['key'])
        sorted_data.append(sort_result)

    sorting(data)
    return sorted_data


def sorting_data(data):
    sorted_data = []
    def sorting(d):
        result = lambda i: sorting(i['value']) if isinstance(i['value'], list) else i['key']
        print(result)
        sort_result = sorted(d, key = result)

        # for item in d:
        #     if isinstance(item['value'], list):
        #         sorting(item['value'])
    #    sort_result = sorted(item, key = lambda i: item['key']) # noqa
        sorted_data.append(sort_result)
        return sorted_data

    sorting(data)
    return sorted_data


print(for_sorting_data(y))





# def sortedDeep(d):
#     def makeTuple(v): return (*v,) if isinstance(v,(list,dict)) else (v,)
#
#     if isinstance(d,list):
#         return sorted( map(sortedDeep,d) ,key=makeTuple )
#     if isinstance(d,dict):
#         return { k: sortedDeep(d[k]) for k in sorted(d)}
#     return d
#
# print(sortedDeep(a))

# import json
# def convert(d):
#   # sort nested lists
#   sort_func = lambda v: v if isinstance(v, str) else sorted(v)
#   y = {k:sort_func(v) for k, v in d.items()}
#   # using JSON to sort dictionary
#   return json.dumps(y, sort_keys=True, indent=2)
#
# print(convert(z))


#
#
# print(sorting(a))

# ttest()
