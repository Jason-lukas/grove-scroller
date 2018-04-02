def add(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Trying to add tuples of different lengths")
    return tuple(sum(i) for i in zip(t1, t2))


def mult(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Trying to multiply tuples of different lengths")
    return tuple(x * y for x, y in zip(t1, t2))