def make_matrix(size: tuple | int, value: int = 0) -> list[list[int]]:
    arr = []
    tuple_size = (size, size) if isinstance(size, int) else size

    for i in range(tuple_size[1]):
        arr.append([])
        for n in range(tuple_size[0]):
            arr[i].append(value)

    return arr
