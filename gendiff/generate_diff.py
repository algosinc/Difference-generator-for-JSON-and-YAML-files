import json
import yaml
from os import path
from gendiff.constants import \
    ALL, ADDED, CHANGED, NESTED, REMOVED, UNCHANGED, VALUE, NEW_VALUE, STATE, STYLISH, PLAIN, JSON
from gendiff.scripts.formatters.stylish import stylish_formatter


def format_output(diff, formatter_style):
    if formatter_style == STYLISH:
        result = stylish_formatter(diff)
        return result

    if formatter_style == PLAIN:
        return stylish_formatter(diff)

    if formatter_style == JSON:
        return stylish_formatter(diff)

    else:
        print(f'Wrong output format: {formatter_style}. Supported formats: {STYLISH}, {PLAIN}, {JSON}'.format)


def generate_diff(first_file, second_file, formatter_style):
    """
    :param first_file:
    :param second_file:
    :param formatter_style:
    :return:
    """
    with open(first_file) as f1, open(second_file) as f2:
        _, file_type = path.splitext(first_file)

        if file_type == '.json':
            first = json.load(f1)
            second = json.load(f2)

        if file_type == '.yml' or file_type == '.yaml':
            first = yaml.safe_load(f1)
            second = yaml.safe_load(f2)

        result_diff = get_diff(first, second)
        return format_output(result_diff, formatter_style)


def get_keys(first, second):
    """
    Create a dict with keys: all, added in removed.
    """
    keys_1 = set(first.keys())
    keys_2 = set(second.keys())
    keys = {
        ALL: sorted(list(keys_1 | keys_2)),
        ADDED: list(keys_2 - keys_1),
        REMOVED: list(keys_1 - keys_2)
    }
    return keys


def get_diff(first, second=None):       # noqa C901
    """
    Creating diff in intermediate format: { key: {state, value or old_value, new_value} }
    """
    if not isinstance(first, dict):
        return first

    if second is None:
        second = first

    all_keys = get_keys(first, second)[ALL]
    removed_keys = get_keys(first, second)[REMOVED]
    added_keys = get_keys(first, second)[ADDED]

    result_diff = {}

    for key in all_keys:
        if key in added_keys:
            result_diff[key] = {
                STATE: ADDED,
                VALUE: get_diff(second[key])  # make recursion
            }

        elif key in removed_keys:
            result_diff[key] = {
                STATE: REMOVED,
                VALUE: get_diff(first[key])
            }

        else:
            if first[key] == second[key]:
                result_diff[key] = {
                    STATE: UNCHANGED,
                    VALUE: get_diff(first[key])
                }

            elif not isinstance(first[key], dict) or not isinstance(second[key], dict):
                result_diff[key] = {
                    STATE: CHANGED,
                    VALUE: get_diff(first[key]),
                    NEW_VALUE: get_diff(second[key])
                }

            else:
                result_diff[key] = {
                    STATE: NESTED,
                    VALUE: get_diff(first[key], second[key]),
                }
    return result_diff
