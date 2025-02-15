def gen_fib():
    """生成无限斐波那契数列的生成器

    Yields:
        int: 斐波那契数列的下一个值，从0开始
        生成机制：每次将当前值与上一个增量相加，并更新增量为前一个当前值

    Examples:
        >>> fib = gen_fib()
        >>> [next(fib) for _ in range(10)]
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

next(filter(lambda n: n > 2024, gen_fib()))



def differences(t):
    """生成相邻元素的差值序列

    Args:
        t (iterator): 数值类型的迭代器

    Yields:
        int: 相邻元素的差值（后一个元素减前一个元素）

    Examples:
        >>> list(differences(iter([5, 2, -100, 103])))
        [-3, -102, 203]
        >>> next(differences(iter([39, 100])))
        61
    """
    "*** YOUR CODE HERE ***"
    last_x = next(t)
    for x in t:
        yield x - last_x
        last_x = x

def partition_gen(n, m):
    """生成所有使用不超过m的整数相加得到n的分区表达式

    Args:
        n (int): 需要分割的目标数，必须大于0
        m (int): 允许使用的最大加数，必须大于0

    Yields:
        str: 以'+'连接的加法表达式，表示一个合法的分区组合

    Examples:
        >>> for partition in sorted(partition_gen(6, 4)):
        ...     print(partition)
        1 + 1 + 1 + 1 + 1 + 1
        1 + 1 + 1 + 1 + 2
        1 + 1 + 1 + 3
        1 + 1 + 2 + 2
        1 + 1 + 4
        1 + 2 + 3
        2 + 2 + 2
        2 + 4
        3 + 3

    实现原理：
        1. 当n等于m时，直接生成m本身
        2. 递归生成包含m的组合：n-m的分区组合加上m
        3. 递归生成不包含m的组合：使用m-1的最大值
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(n)
    if n - m > 0:
        "*** YOUR CODE HERE ***"
        for p in partition_gen(n -m, m):
            yield p + ' + ' + str(m)
    if m > 1:
        "*** YOUR CODE HERE ***"
        yield from partition_gen(n, m-1)
