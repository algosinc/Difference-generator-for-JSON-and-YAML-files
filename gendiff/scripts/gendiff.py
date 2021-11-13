#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import argparse
import yaml


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


def yaml_compare(first_yaml, second_yaml):
    keys = set(first_yaml.keys())
    keys_list = list(keys.union(set(second_yaml.keys())))
    keys_list.sort()
    result = []
    for key in keys_list:
        if (key in first_yaml) and (key in second_yaml):
            if first_yaml[key] == second_yaml[key]:             # no changes
                result.append(f'  {yaml_encode(key)}: {yaml_encode(first_yaml[key])}')
            if first_yaml[key] != second_yaml[key]:             # value changed
                result.append(f'- {yaml_encode(key)}: {yaml_encode(first_yaml[key])}')
                result.append(f'+ {yaml_encode(key)}: {yaml_encode(second_yaml[key])}')
            continue
        if (key in first_yaml) and not (key in second_yaml):
            result.append(f'- {yaml_encode(key)}: {yaml_encode(first_yaml[key])}')  # remove item
            continue
        else:
            result.append(f'+ {yaml_encode(key)}: {yaml_encode(second_yaml[key])}')  # new item
    return '\n'.join(result)


def json_encode(value_in_json):
    return json.JSONEncoder().encode(value_in_json)


def yaml_encode(value_in_yaml):
    return yaml.safe_dump(value_in_yaml)[:-5]


def generate_diff(first_file, second_file, file_type):
    with open(first_file) as f1:
        with open(second_file) as f2:
            if file_type == 'json':
                first_json = json.load(f1)
                second_json = json.load(f2)
                return json_compare(first_json, second_json)
            if file_type == 'yaml':
                first_yaml = yaml.safe_load(f1)
                second_yaml = yaml.safe_load(f2)
                return yaml_compare(first_yaml, second_yaml)


# def test():
#     first_file = r'../../tests/fixtures/yaml/file1.yml'
#     second_file = r'../../tests/fixtures/yaml/file2.yml'
#     print(generate_diff(first_file, second_file, 'yaml'))
#
#
# test()


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument('-f', '--format', dest='format', default='json',
                        help='set format of output')
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
