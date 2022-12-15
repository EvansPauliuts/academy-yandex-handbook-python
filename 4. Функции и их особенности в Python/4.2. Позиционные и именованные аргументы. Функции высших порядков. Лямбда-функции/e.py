from typing import Any


def to_string(*a: Any, sep: Any = ' ', end: Any = '\n') -> str:
    res = f'{sep}'.join([str(i) for i in a])
    return res + f'{end}'
