import re


def time(time_str: str) -> float:
    """
    Converts a formatted time string into the value in milliseconds.
    :param time_str:
    :return:

    Examples:
    "5min" -> 300000
    "0.1min" -> 10000
    "15sec" -> 15000
    "500ms" -> 500
    """
    match = re.match(r'(\d+(.\d+)?)\s?(min|sec|ms)?', time_str)
    if not match:
        return 0

    digits = float(match.group(1))

    if time_str.endswith('min'):
        return digits * 60 * 1000
    elif time_str.endswith('sec'):
        return digits * 1000
    else:
        return digits
