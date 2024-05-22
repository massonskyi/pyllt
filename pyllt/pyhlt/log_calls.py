import functools

__all__ = ['log_calls']
__version__ = '0.1.0'
__description__ = 'Логирует вызовы функции, включая аргументы и возвращаемое значение.'


def log_calls(func):
    @functools.wraps(func)
    def wrapper_log_calls(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper_log_calls


if __name__ == "__main__":
    @log_calls
    def add(a, b):
        return a + b


    add(2, 3)
