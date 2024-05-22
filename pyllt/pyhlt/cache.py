import functools

__all__ = ['log_calls']
__version__ = '0.1.0'
__description__ = 'Кэширует результаты функции с ограничением на размер кэша.'


def lru_cache(maxsize=128):
    def decorator_lru_cache(func):
        cache = {}
        order = []

        @functools.wraps(func)
        def wrapper_lru_cache(*args, **kwargs):
            key = (args, frozenset(kwargs.items()))
            if key in cache:
                order.remove(key)
                order.append(key)
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            order.append(key)
            if len(order) > maxsize:
                oldest_key = order.pop(0)
                del cache[oldest_key]
            return result

        return wrapper_lru_cache

    return decorator_lru_cache


if __name__ == '__main__':
    @lru_cache(maxsize=2)
    def compute(a, b):
        return a + b


    print(compute(1, 2))
    print(compute(2, 3))
    print(compute(1, 2))  # Should be from cache
    print(compute(3, 4))
    print(compute(2, 3))  # Should be from cache
