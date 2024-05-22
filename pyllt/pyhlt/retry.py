import functools
import time

__all__ = ['retry']
__version__ = '0.1.0'
__description__ = 'Повторяет вызов функции определенное количество раз в случае ошибки.'


def retry(retries=3, delay=1):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper_retry(*args, **kwargs):
            last_exception = None
            for _ in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    time.sleep(delay)
            raise last_exception

        return wrapper_retry

    return decorator_retry


if __name__ == "__main__":
    @retry(retries=3, delay=2)
    def test_func():
        print("Trying...")
        raise ValueError("An error occurred")


    test_func()
