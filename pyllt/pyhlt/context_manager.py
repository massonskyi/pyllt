__alL__ = ['contextmanager']
__version__ = '0.1.0'
__description__ = 'Позволяет функции использовать контекстный менеджер.'

import contextlib
import functools


def contextmanager(func):
    @functools.wraps(func)
    def wrapper_contextmanager(*args, **kwargs):
        return contextlib.contextmanager(func)(*args, **kwargs)

    return wrapper_contextmanager


if __name__ == '__main__':
    @contextmanager
    def managed_resource(name):
        print(f"Acquiring resource: {name}")
        yield
        print(f"Releasing resource: {name}")


    with managed_resource("database connection"):
        print("Using resource")
