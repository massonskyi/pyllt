__all__ = ['ternary_search']


def ternary_search(a, b, f, eps=1e-9):
    """
    Ternary search algorithm to find the minimum value of a unimodal function f
    within the range [a, b].

    Parameters:
    a (float): Left boundary of the search interval.
    b (float): Right boundary of the search interval.
    f (function): The unimodal function to be minimized.
    eps (float): The precision of the result.

    Returns:
    float: The x value that minimizes the function f within [a, b].
    """
    while b - a > eps:
        m1 = a + (b - a) / 3
        m2 = b - (b - a) / 3
        f1 = f(m1)
        f2 = f(m2)

        if f1 < f2:
            b = m2
        else:
            a = m1

    return (a + b) / 2


if __name__ == '__main__':
    f = lambda x: (x - 2) ** 2
    a = 0
    b = 5
    result = ternary_search(a, b, f)
    print("The minimum value is at x =", result)
