import json


def json_formatter(diff):
    """Convert diff to the JSON format.
    Args:
        diff: generated difference between two files.
    Returns:
        Difference in classic json format.
    """
    return json.dumps(diff)
