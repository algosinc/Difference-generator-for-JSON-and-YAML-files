#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import argparse


def compare(first_json, second_json):
    keys = set(first_json.keys())
    keys_list = list(keys.union(set(second_json.keys())))
    keys_list.sort()
    result = ['{', ]
    for key in keys_list:
        if (key in first_json) and (key in second_json):
            if first_json[key] == second_json[key]:             # no changes
                result.append(f'    {encode(key)}: {encode(first_json[key])}')
            if first_json[key] != second_json[key]:             # value changed
                result.append(f'  - {encode(key)}: {encode(first_json[key])}')
                result.append(f'  + {encode(key)}: {encode(second_json[key])}')
            continue
        if (key in first_json) and not (key in second_json):
            result.append(f'  - {encode(key)}: {encode(first_json[key])}')  # noqa # remove item
            continue
        else:
            result.append(f'  + {encode(key)}: {encode(second_json[key])}')  # noqa # new item
    result.append('}')
    return '\n'.join(result)


def encode(value_in_json):
    return json.JSONEncoder().encode(value_in_json)


def generate_diff(first_file, second_file, format):
    with open(first_file) as f1:
        with open(second_file) as f2:
            first_json = json.load(f1)
            second_json = json.load(f2)
            return compare(first_json, second_json)


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
