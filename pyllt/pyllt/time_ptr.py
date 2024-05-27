import contextlib
import functools
import time

__all__ = ['TimeitPtr']


class TimeitPtr(contextlib.ContextDecorator):
    def __init__(self, t=0.0, time_func=None):
        self.t = t
        self.time_func = time_func or time.time

    def __enter__(self):
        self.start = self.time_func()
        return self

    def __exit__(self, type, value, traceback):
        self.dt = self.time_func() - self.start
        self.t += self.dt

    def __str__(self):
        return f"Elapsed time is {self.t} s"

    @staticmethod
    def timeit(func):
        @functools.wraps(func)
        def wrapper_timeit(*args, **kwargs):
            start_time = time.time()  # Record the start time
            result = func(*args, **kwargs)  # Call the function
            end_time = time.time()  # Record the end time
            elapsed_time = end_time - start_time  # Calculate the elapsed time
            print(
                f"Function {func.__name__!r} with arguments {args!r} and keywords arguments {kwargs!r} executed in {elapsed_time:.4f} seconds")
            return result  # Return the result of the function

        return wrapper_timeit


if __name__ == "__main__":
    # Пример использования:
    # Измерение времени выполнения блока кода
    with TimeitPtr() as timer:
        time.sleep(1)

    print(timer)  # Выведет "Elapsed time is 1.0 s"


    # Измерение времени выполнения конкретной функции
    @TimeitPtr.timeit
    def my_function():
        time.sleep(1)


    my_function()
    print()  # Выведет "Elapsed time is 1.0 s"
