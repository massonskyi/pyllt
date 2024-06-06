__all__ = ['linear_search']


def linear_search(arr: list, x: object):
    """
    Linear search algorithm
    :param arr: list
    :param x: int
    :return: int
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = 10
    print(linear_search(arr, x))
