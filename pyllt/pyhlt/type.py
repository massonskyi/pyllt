__alL__ = ['type_check']
__version__ = '0.1.0'
__description__ = 'Проверяет типы аргументов функции.'

import functools


def type_check(*types):
    def decorator_type_check(func):
        @functools.wraps(func)
        def wrapper_type_check(*args, **kwargs):
            if len(args) != len(types):
                raise ValueError("Argument count does not match")
            for a, t in zip(args, types):
                if not isinstance(a, t):
                    raise TypeError(f"Expected {t}, got {type(a)}")
            return func(*args, **kwargs)

        return wrapper_type_check

    return decorator_type_check


if __name__ == "__main__":
    @type_check(int, int)
    def add(a, b):
        return a + b


    print(add(2, 3))  # Valid
    # print(add(2, '3'))  # Invalid
