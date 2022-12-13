arr_new = []


def modern_print(name: str) -> None:
    if name not in arr_new:
        print(name)

    arr_new.append(name)
