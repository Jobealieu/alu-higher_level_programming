#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples element-wise, returning a tuple with 2 integers."""
    # Handle tuple_a: get first two elements or use 0 for missing ones
    if len(tuple_a) == 0:
        a1, a2 = 0, 0
    elif len(tuple_a) == 1:
        a1, a2 = tuple_a[0], 0
    else:
        a1, a2 = tuple_a[0], tuple_a[1]

    # Handle tuple_b: get first two elements or use 0 for missing ones
    if len(tuple_b) == 0:
        b1, b2 = 0, 0
    elif len(tuple_b) == 1:
        b1, b2 = tuple_b[0], 0
    else:
        b1, b2 = tuple_b[0], tuple_b[1]

    # Return new tuple with the sum of corresponding elements
    return (a1 + b1, a2 + b2)
