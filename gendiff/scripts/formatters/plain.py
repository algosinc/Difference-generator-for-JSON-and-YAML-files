#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Any
from gendiff.constants import \
    ADDED, CHANGED, NESTED, REMOVED, VALUE, NEW_VALUE, STATE


def plain_formatter(diff: dict) -> str:
    """
    Take a diff in intermediate format: { key: {state, value or old_value, new_value} }
    and format it in thesis-like format with statements about adding, updating and removal, like:

    Property 'common.follow' was added with value: false
    Property 'common.setting2' was removed
    Property 'common.setting3' was updated. From true to null
    """
    lines = []

    def _walk(node: dict, parent_key: str):
        for key, item in node.items():
            state = item.get(STATE)
            value = item.get(VALUE)
            full_path = '.'.join([parent_key, key])
            if state == NESTED:
                _walk(value, full_path)     # recursive call

            if state == ADDED:
                lines.append(get_added_line(full_path, value))

            if state == REMOVED:
                lines.append(get_removed_line(full_path, value))

            if state == CHANGED:
                new_value = item.get(NEW_VALUE)
                lines.append(get_changed_line(full_path, value, new_value))

    _walk(diff, '')
    return '\n'.join(lines)


def get_added_line(path: str, value: Any) -> str:
    """ Get formatted string by template for added line """
    return f"Property '{path[1:]}' was added with value: {convert_value(value)}"


def get_removed_line(path: str, value: Any) -> str:
    """ Get formatted string by template for removed line """
    return f"Property '{path[1:]}' was removed"


def get_changed_line(path: str, value: Any, new_value: Any) -> str:
    """ Get formatted string by template for updated line """
    return f"Property '{path[1:]}' was updated. From {convert_value(value)} to {convert_value(new_value)}"


def convert_value(value: Any) -> str:
    """ Convert Python values to JSON style """
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value
