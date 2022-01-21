from gendiff.constants import ADDED, CHANGED, INDENT, NESTED, REMOVED, UNCHANGED, VALUE, NEW_VALUE, STATE
from gendiff.scripts.formatters.tools import convert
from tests.fixtures.formatters.diff_fixture import data as testdata


def stylish_formatter(tree):
    return '\n'.join(formatter(tree))


def _add_tab(state, depth, key):
    signs = {ADDED: '+', REMOVED: '-', UNCHANGED: ' ', NESTED: ' ', CHANGED: '-'}
    return f'{INDENT * depth}{signs.get(state)} {key}: ' + '{'


def _remove_tab(depth):
    return f'{INDENT * depth}' + '}'


def _make_line(state, depth, key, val):  # make in format line
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


def formatter(tree, depth=0):       # noqa C901
    lines = ['{']

    if not isinstance(tree, dict):
        return tree

    def _walk(node, depth):

        for key in node.keys():
            data = node[key]
            state = data.get(STATE)
            value = data.get(VALUE)
            new_value = data.get(NEW_VALUE)

            if state == CHANGED:
                changed_state(lines, depth, key, value, new_value)
                continue

            if not isinstance(value, dict):  # processing leaf node
                lines.append(_make_line(state=state, depth=depth + 1, key=key, val=value))
                continue

            lines.append(_add_tab(state=state, depth=depth + 1, key=key))  # add level
            _walk(value, depth + 2)  # step inside recursion
            lines.append(_remove_tab(depth + 2))  # remove level

    _walk(tree, depth)
    lines.append('}')
    return lines


def changed_state(lines, depth, key, value, new_value):
    # for CHANGED, we make line, what was removed and make line with added items
    if isinstance(value, dict):  # processed nested items
        lines.append(_add_tab(REMOVED, depth + 1, key))
        lines.extend(formatter(value, depth + 2)[1:-1])  # and remove brackets
        lines.append(_remove_tab(depth + 2))
    else:  # processing leaf node
        lines.append(_make_line(state=REMOVED, depth=depth + 1, key=key, val=formatter(value)))

    if isinstance(new_value, dict):  # processed nested items
        lines.append(_add_tab(ADDED, depth + 1, key))
        lines.extend(formatter(new_value, depth + 2)[1:-1])
        lines.append(_remove_tab(depth + 2))
    else:  # processing leaf node
        lines.append(_make_line(state=ADDED, depth=depth + 1, key=key, val=formatter(new_value)))


def main():
    print(stylish_formatter(testdata))


if __name__ == '__main__':
    main()
