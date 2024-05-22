import time
import functools

__alL__ = ['timeit']
__version__ = '0.1.0'
__description__ = 'Измеряет время выполнения функции.'


def timeit(func):
    @functools.wraps(func)
    def wrapper_timeit(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # Record the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time
        print(f"Function {func.__name__!r} with arguments {args!r} and keywords arguments {kwargs!r} executed in {elapsed_time:.4f} seconds")
        return result  # Return the result of the function

    return wrapper_timeit


if __name__ == "__main__":
    # Usage example
    @timeit
    def example_function(n):
        total = 0
        for i in range(n):
            total += i
        return total


    result = example_function(1000000)
    print(f"Result: {result}")
