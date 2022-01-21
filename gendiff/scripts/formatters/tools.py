
def convert(value):
    """convert views of python values to json"""

    if value is None:
        return 'null'
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    return str(value)
