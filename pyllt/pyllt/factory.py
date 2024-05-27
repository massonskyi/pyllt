__all__ = ['CallbackFactory']


class CallbackFactory(object):
    """
    Factory class to create objects
    """

    def __init__(self):
        """
        Constructor of the class Factory
        """
        self._creators = {}

    def register(self, event: str, callback: callable):
        """
        Register a new event
        :param event: event name
        :param callback: callback function
        :return:
        """
        self._creators[event] = callback

    def create(self, event: str, *args, **kwargs):
        """
        Create an object
        :param event: event name
        :param args: arguments
        :param kwargs: keyword arguments
        :return:
        """
        if event in self._creators:
            return self._creators[event](*args, **kwargs)
        else:
            raise ValueError("Event {} not registered".format(event))


if __name__ == "__main__":
    class MyClass:
        def __init__(self, value):
            self.value = value


    callbacks = CallbackFactory()
    callbacks.register('MyClass', MyClass)
    callbacks.register('add', lambda x, y: x + y)

    obj = callbacks.create('MyClass', 10)
    callbacks = [callbacks.create("add", it, ij) for it, ij in zip(range(0, 10), range(1, 11))]
    for callback in callbacks:
        print(callback)  # Output: 1,3,5,7,9,11,13,15,17,19

