__all__ = ['Singleton']


class SingletonMeta(type):
    """
    Metaclass for singleton classes.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Singleton class constructor.
        :param args: arguments
        :param kwargs: keyword arguments
        :return: singleton instance
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    Singleton class.
    """
    pass


if __name__ == "__main__":
    # Пример использования
    class MyClass(Singleton):
        def __init__(self, value):
            self.value = value


    singleton1 = MyClass(10)
    singleton2 = MyClass(20)

    print(singleton1.value)  # Output: 10
    print(singleton1 is singleton2)  # Output: True