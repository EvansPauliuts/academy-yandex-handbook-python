from typing import Tuple


def merge(a: Tuple, b: Tuple) -> Tuple:
    size_1 = len(a)
    size_2 = len(b)

    res = []
    i, j = 0, 0

    while i < size_1 and j < size_2:
        if a[i] < b[j]:
            res.append(a[i])
            i += 1

        else:
            res.append(b[j])
            j += 1

    res.extend(a[i:])
    res.extend(b[j:])

    return tuple(res)
