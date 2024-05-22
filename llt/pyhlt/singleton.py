import functools

__all__ = ['singleton']
__version__ = '0.1.0'
__description__ = 'Обеспечивает, что класс имеет только один экземпляр.'


def singleton(cls):
    instances = {}

    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


if __name__ == '__main__':
    @singleton
    class Database:
        def __init__(self, val=20):
            self.val = val
            print("Database connection established")


    db1 = Database()
    db2 = Database()

    print(db1 is db2)  # Output: True
    print(db1.val == db2.val)  # Output: True
