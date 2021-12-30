from itertools import chain

from gendiff.constants import (
    ADDED,
    CHANGED,
    INDENT,
    NESTED,
    REMOVED,
    UNCHANGED,
    VALUE,
    NEW_VALUE, STATE
)

tree = {'common': {'state': 'nested', 'value': {'follow': {'state': 'added', 'value': False}, 'setting1': {'state': 'unchanged', 'value': 'Value 1'}, 'setting2': {'state': 'removed', 'value': 200}, 'setting3': {'state': 'changed', 'value': True, 'new_value': None}, 'setting4': {'state': 'added', 'value': 'blah blah'}, 'setting5': {'state': 'added', 'value': {'key5': {'state': 'unchanged', 'value': 'value5'}}}, 'setting6': {'state': 'nested', 'value': {'doge': {'state': 'nested', 'value': {'wow': {'state': 'changed', 'value': '', 'new_value': 'so much'}}}, 'key': {'state': 'unchanged', 'value': 'value'}, 'ops': {'state': 'added', 'value': 'vops'}}}}}, 'group1': {'state': 'nested', 'value': {'baz': {'state': 'changed', 'value': 'bas', 'new_value': 'bars'}, 'foo': {'state': 'unchanged', 'value': 'bar'}, 'nest': {'state': 'changed', 'value': {'key': {'state': 'unchanged', 'value': 'value'}}, 'new_value': 'str'}}}, 'group2': {'state': 'removed', 'value': {'abc': {'state': 'unchanged', 'value': 12345}, 'deep': {'state': 'unchanged', 'value': {'id': {'state': 'unchanged', 'value': 45}}}}}, 'group3': {'state': 'added', 'value': {'deep': {'state': 'unchanged', 'value': {'id': {'state': 'unchanged', 'value': {'number': {'state': 'unchanged', 'value': 45}}}}}, 'fee': {'state': 'unchanged', 'value': 100500}}}}


def convert(value):   # convert views of python values to json
    if value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    return str(value)

def _make_line(state, depth, key, val, new_val=None):  # OK
    template = '{ind}{sign} {key}: {value}'

    signs = {
        ADDED: '+',
        REMOVED: '-',
        UNCHANGED: ' ',
        NESTED: ' '
    }

    return template.format(
        ind=INDENT * depth,
        sign=signs.get(state),
        key=key,
        value=convert(val)
    )


def _add_tab(state, depth, key):
    signs = {ADDED: '+', REMOVED: '-', UNCHANGED: ' ', NESTED: ' ', CHANGED: '-'}
    return '{ind}{sign} {key}: '.format(ind=INDENT * depth, sign=signs.get(state), key=key) + '{'


def _remove_tab(depth):
    return '{ind}'.format(ind=INDENT * depth) + '}'


def stylish_format(tree, depth=0):
    lines = ['{']
#    lines = []

    if not isinstance(tree, dict):
        return tree

    def _walk(node, depth):

        for key, node_val in sorted(node.items()):
            data = node[key]
            state = data.get(STATE)
            value = data.get(VALUE)
            new_value = data.get(NEW_VALUE)

            if state == CHANGED:
                if isinstance(value, dict):
                    lines.append(_add_tab(REMOVED, depth + 1, key))
                    lines.extend(stylish_format(value, depth + 2)[1:-1])
                    lines.append(_remove_tab(depth + 2))
                else:
                    lines.append(_make_line(state=REMOVED, depth=depth + 1, key=key, val=stylish_format(value)))

                if isinstance(new_value, dict):
                    lines.append(_add_tab(state, depth + 1, key))
                    lines.extend(stylish_format(new_value, depth + 2)[1:-1])
                    lines.append(_remove_tab(depth + 2))
                else:
                    lines.append(_make_line(state=ADDED, depth=depth + 1, key=key, val=stylish_format(new_value)))
                continue

            if not isinstance(value, dict):  # обработка конечного узла
                result = _make_line(state=state, depth=depth + 1, key=key, val=value, new_val=new_value)
                lines.append(result)
                continue

            lines.append(_add_tab(state=state, depth=depth + 1, key=key))  # add level
            _walk(value, depth + 2)
            lines.append(_remove_tab(depth + 2))  # remove level

    _walk(tree, depth)
    lines.append('}')
    return lines

res = stylish_format(tree)
for i in res:
    print(i)

