from gendiff.constants import ADDED, CHANGED, INDENT, NESTED, REMOVED, UNCHANGED, VALUE, NEW_VALUE, STATE


def stylish_formatter(tree):
    return '\n'.join(formatter(tree))


def convert(value):   # convert views of python values to json
    if value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    return str(value)


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


def _add_tab(state, depth, key):
    signs = {ADDED: '+', REMOVED: '-', UNCHANGED: ' ', NESTED: ' ', CHANGED: '-'}
    return '{ind}{sign} {key}: '.format(ind=INDENT * depth, sign=signs.get(state), key=key) + '{'


def _remove_tab(depth):
    return '{ind}'.format(ind=INDENT * depth) + '}'


def formatter(tree, depth=0):       # noqa C901
    lines = ['{']

    if not isinstance(tree, dict):
        return tree

    def _walk(node, depth):

        for key, node_val in node.items():
            data = node[key]
            state = data.get(STATE)
            value = data.get(VALUE)
            new_value = data.get(NEW_VALUE)

            if state == CHANGED:
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
                continue

            if not isinstance(value, dict):  # processing leaf node
                result = _make_line(state=state, depth=depth + 1, key=key, val=value)
                lines.append(result)
                continue

            lines.append(_add_tab(state=state, depth=depth + 1, key=key))  # add level
            _walk(value, depth + 2)  # step inside recursion
            lines.append(_remove_tab(depth + 2))  # remove level

    _walk(tree, depth)
    lines.append('}')
    return lines
