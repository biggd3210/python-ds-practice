def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """

    min_max = []

    d_lst = sorted(d.keys())

    min_max.append(d_lst[0])
    min_max.append(d_lst[len(d_lst) - 1])

    return tuple(min_max)

# recommended:
# keys = d.keys()
# return (min(keys), max(keys))