__all__ = ['binary_search']


def binary_search(arr: list, target: object, start: int = None, end: int = None) -> int:
    """
    Binary search algorithm for target in arr
    :param arr:
    :param target:
    :param start:
    :param end:
    :return:
    """
    if start is None:
        start = 0

    if end is None:
        end = len(arr) - 1

    if start > end:
        return -1

    mid = (start + end) // 2
    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)

    else:
        return binary_search(arr, target, mid + 1, end)


if __name__ == '__main__':
    arr = [it for it in range(0, 9999999, 1)]
    target = 5643

    print(binary_search(arr, target))
