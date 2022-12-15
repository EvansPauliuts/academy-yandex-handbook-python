import math

from functools import reduce
from typing import Any


def gcd(*args: Any) -> Any:
    return reduce(math.gcd, args)
