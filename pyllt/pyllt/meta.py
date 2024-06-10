class Meta(type):
    """
    Metaclass for the class.
    """

    def __new__(cls, name, bases, attrs):
        """
        Create a new class.
        """
        # Get the base class.
        cls = super().__new__(cls, name, bases, attrs)
        # Добавляем новый атрибут
        cls.registry = {}
        return cls


class Base(metaclass=Meta):
    """
    Base class for the class.
    """

    def __init_subclass__(cls, **kwargs):
        """
        Initialize the subclass.
        """
        # Добавляем новый атрибут
        super().__init_subclass__(**kwargs)
        # Регистрируем подклассы
        cls.registry[cls.__name__] = cls


if __name__ == '__main__':
    class MyClass(Base):
        pass


    class AnotherClass(Base):
        pass


    print(Base.registry['MyClass'].__dict__)  # {'__module__': '__main__', '__doc__': None, 'pyllt': <function __init_subclass__ at 0x7f9b8b4b9e10>, '__new__': <function Meta.__new__ at 0x7f9b8b4])  # {'MyClass': <class '__main__.MyClass'>, 'AnotherClass': <class '__main__.AnotherClass'>}