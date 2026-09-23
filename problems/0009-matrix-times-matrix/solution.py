def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if not a or not a[0] or not b or not b[0]:
        return -1

    if any(len(row) != len(a[0]) for row in a) or any(len(row) != len(b[0]) for row in b):
        return -1

    if len(a[0]) != len(b):
        return -1

    b_cols = list(zip(*b))
    c = [
        [sum(x * y for x, y in zip(row_a, col_b)) for col_b in b_cols]
        for row_a in a
    ]
    return c