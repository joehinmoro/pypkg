def fibonacci(n):
    """
    Calculate nth term in fibonacci sequence
    
    Args:
        n (int): nth term in fibonacci sequence to calculate
    
    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms
    
    Examples:
        >>> fibonacci(1)
        1        
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    """
    # n <=1
    if n <= 1: return n

    lst = [0, 1]

    for num in range(n - 1):
        lst.append(lst[-1] + lst[-2])

    return lst[-1]


def sort_n_slice(itr, n, desc=False):
    """Return the top n items in an array, in descending order.

    Args:
        items (array): list or array-like object containing numerical values.
        n (int): number of top items to return.

    Returns:
        array: top n items, in descending order.

    Examples:
        >>> top_n([8, 3, 2, 7, 4], 3)
        [8, 7, 3]
    """

    itr.sort(reverse=desc)
    return itr[:n]
