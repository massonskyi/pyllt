__alL__ = ['ensure_method_exists']
__version__ = '0.1.0'
__description__ = 'Декоратор для методов класса, позволяющий обойти отсутствие метода в родительском классе.'


def ensure_method_exists(method_name):
    def decorator_ensure_method_exists(cls):
        if not hasattr(cls, method_name):
            raise TypeError(f"Class {cls.__name__} must implement method {method_name}")
        return cls

    return decorator_ensure_method_exists


if __name__ == '__main__':
    @ensure_method_exists('process')
    class Processor:
        def process(self):
            print("Processing...")

    # Processor()  # Will not raise an error
