#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import yaml
from os import path
from gendiff.constants import \
    ALL, ADDED, CHANGED, NESTED, REMOVED, UNCHANGED, VALUE, NEW_VALUE, STATE, STYLISH, PLAIN, JSON
from gendiff.scripts.formatters.stylish import stylish_formatter
from gendiff.scripts.formatters.plain import plain_formatter
from gendiff.scripts.formatters.json import json_formatter


def format_output(diff: dict, formatter_style: str) -> str:
    """ Starts diff formatting based on the selected formatter """

    print(formatter_style)

    if formatter_style == STYLISH:
        return stylish_formatter(diff)

    if formatter_style == PLAIN:
        return plain_formatter(diff)

    if formatter_style == JSON:
        return json_formatter(diff)

    else:
        print(f'Wrong output format: {formatter_style}. Supported formats: {STYLISH}, {PLAIN}, {JSON}'.format)


def generate_diff(file_path1, file_path2, formatter_style):
    """
    Detects the format of the submitted files, reads data from them,
    converts them into Python objects and runs diff generation.

    Args:
        file_path1: Path to the first file.
        file_path2: Path to the second file.
        formatter_style: Chosen style of diff in CLI.

    Returns:
        Differences between two files.
    """
    with open(file_path1) as f1, open(file_path2) as f2:
        _, file_type = path.splitext(file_path1)

        if file_type == '.json':
            first_dict = json.load(f1)
            second_dict = json.load(f2)

        if file_type == '.yml' or file_type == '.yaml':
            first_dict = yaml.safe_load(f1)
            second_dict = yaml.safe_load(f2)

        return format_output(get_diff(first_dict, second_dict), formatter_style)


def get_keys(first_dict: dict, second_dict: dict) -> dict:
    """
    Create the dict with keys: all, added in removed.
    """
    keys_1 = set(first_dict.keys())
    keys_2 = set(second_dict.keys())
    keys = {
        ALL: sorted(list(keys_1 | keys_2)),
        ADDED: list(keys_2 - keys_1),
        REMOVED: list(keys_1 - keys_2)
    }
    return keys


def get_diff(first_dict: dict, second_dict=None) -> dict:       # noqa C901
    """
    Compare two dicts and create the diff in intermediate format:
    { key: {state, value or old_value, new_value} }
    """
    if not isinstance(first_dict, dict):     # returns the end value
        return first_dict

    if second_dict is None:      # for case when only one of two compared values is nested
        second_dict = first_dict

    all_keys = sorted(get_keys(first_dict, second_dict)[ALL])
    removed_keys = get_keys(first_dict, second_dict)[REMOVED]
    added_keys = get_keys(first_dict, second_dict)[ADDED]

    result_diff = {}

    for key in all_keys:
        if key in added_keys:
            result_diff[key] = {
                STATE: ADDED,
                VALUE: get_diff(second_dict[key])
            }

        elif key in removed_keys:
            result_diff[key] = {
                STATE: REMOVED,
                VALUE: get_diff(first_dict[key])
            }

        else:
            if first_dict[key] == second_dict[key]:
                result_diff[key] = {
                    STATE: UNCHANGED,
                    VALUE: get_diff(first_dict[key])
                }

            elif not isinstance(first_dict[key], dict) or not isinstance(second_dict[key], dict):
                result_diff[key] = {
                    STATE: CHANGED,
                    VALUE: get_diff(first_dict[key]),
                    NEW_VALUE: get_diff(second_dict[key])
                }

            else:
                result_diff[key] = {
                    STATE: NESTED,
                    VALUE: get_diff(first_dict[key], second_dict[key]),
                }
    return result_diff
