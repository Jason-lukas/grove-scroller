def add(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Trying to add tuples of different lengths")
    return tuple(sum(i) for i in zip(t1, t2))


def mult(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Trying to multiply tuples of different lengths")
    return tuple(x * y for x, y in zip(t1, t2))


def clamp(val, min_val, max_val):
    if val <= min_val:
        return min_val
    elif val >= max_val:
        return max_val
    else:
        return val


def lerp(val1, val2, alpha):
    alpha = clamp(float(alpha), 0.0, 1.0)
    return float(val1) + alpha * float(val2 - val1)
