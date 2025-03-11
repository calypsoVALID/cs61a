def smallest_abs_index(s: list) -> list:
    """return a list that contain the index of have smallest absolute value.
    
    >>> s = [-4, -3, -2, 3, 2, 4]
    >>> smallest_abs_index(s)
    [2, 4]
    >>> s = [1, 2, 3, 4, 5]
    >>> smallest_abs_index(s)
    [0]
    """
    min_abs = min(map(abs, s))
    f = lambda i: abs(s[i]) == min_abs
    return list(filter(f, range(len(s))))

    # min_abs = min(map(abs, s))
    # return [i for i in range(len(s)) if min_abs = abs(s[i])]


def largest_adjacent_sum(s: list) -> list:
    """return a list that contain the largest sum of two adjacent elements in list s
    
    >>> s = [-4, -3, -2, 3, 2, 4]
    >>> largest_adjacent_sum(s)
    6
    """
    return max([a + b for a, b in zip(s[:-1], s[1:])])

    # return max([s[i] + s[i + 1] for i in range(len(s) - 1)])

def digit_dict(s: list) -> dict:
    """Map each digit d to the lists of elements in s that end with d.
    
    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    {d: [x for x in s if x % 10 == d] for d in range(10) if any([x % 10 == d for x in s])}

def all_have_an_equal(s: list) -> bool :
    """Does every element equal some other element in s?
    
    >>> all_have_an_equal([-4, -3, -2, 3, 2, 4])
    False
    """
    return all([s[i] in s[:i]+ s[i+1:] for i in range(len(s))])