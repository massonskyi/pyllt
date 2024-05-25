import asyncio


class CallbackFactory:
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

    async def create(self, event: str, *args, **kwargs):
        """
        Create an object asynchronously
        :param event: event name
        :param args: arguments
        :param kwargs: keyword arguments
        :return:
        """
        if event in self._creators:
            callback = self._creators[event]
            return await callback(*args, **kwargs)
        else:
            raise ValueError(f"Event {event} not registered")


# Пример использования
async def example_callback(name):
    await asyncio.sleep(1)
    return f"Hello, {name}!"


async def main():
    factory = CallbackFactory()
    factory.register("greet", example_callback)

    result = await factory.create("greet", "Alice")
    print(result)  # Вывод: Hello, Alice!


asyncio.run(main())
