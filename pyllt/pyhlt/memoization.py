import functools

__all__ = ['memoize']
__version__ = '0.1.0'
__description__ = 'Кэширует результаты вызова функции для повышения производительности.'

def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper_memoize(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return wrapper_memoize


if __name__ == '__main__':
    @memoize
    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)


    print(fibonacci(30))
