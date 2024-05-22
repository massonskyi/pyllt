__all__ = ['SmartPointer']


class SmartPointer(object):
    """
    A smart pointer class.
    """
    def __init__(self, obj: object):
        """
        Initialize the smart pointer.
        :param obj: The object to be managed.
        """
        self.obj = obj

    def __enter__(self):
        """
        Enter the context.
        :return: The object.
        """
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context.
        :param exc_type: The exception type.
        :param exc_val: The exception value.
        :param exc_tb: The exception traceback.
        :return: None.
        """
        del self.obj


if __name__ == '__main__':
    # Пример использования
    class MyClass:
        def __init__(self, value):
            self.value = value


    with SmartPointer(MyClass(10)) as obj:
        print(obj.value)  # Output: 10
