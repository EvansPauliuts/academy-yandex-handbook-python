from typing import Any


def is_palindrome(a: Any) -> bool:
    is_type = any(
        [isinstance(a, list), isinstance(a, tuple)]
    )
    letters = a if is_type else list(str(a))
    is_bool = True

    if isinstance(letters, tuple):
        letters = list(letters)

    for letter in letters:
        if letter == letters[-1]:
            letters.pop(-1)
        else:
            is_bool = False
            break

    return is_bool

