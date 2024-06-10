from typesllt.base.Object import Object
import numpy as np

class Short(Object):
    _value: np.short

    def __init__(self, value=0):
        super().__init__()

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Short({self.value})"

    def __eq__(self, other):
        if isinstance(other, Short):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Short):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Short):
            return self.value <= other.value
        elif isinstance(other, int):
            return self.value <= other
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Short):
            return self.value > other.value
        elif isinstance(other, int):
            return self.value > other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Short):
            return self.value >= other.value
        elif isinstance(other, int):
            return self.value >= other
        else:
            return NotImplemented

    def __hash__(self):
        return hash(self.value)

    def __bool__(self):
        return bool(self.value)

    def __getattr__(self, name):
        raise AttributeError("'Short' object has no attribute '{}'".format(name))

    def __setattr__(self, name, value):
        raise AttributeError("can't set attribute '{}'".format(name))

    def __delattr__(self, name):
        raise AttributeError("can't delete attribute '{}'".format(name))

    def __getitem__(self, key):
        raise TypeError("'Short' object is not subscriptable")

    def __setitem__(self, key, value):
        raise TypeError("'Short' object does not support item assignment")

    def __delitem__(self, key):
        raise TypeError("'Short' object does not support item deletion")

    def __iter__(self):
        return iter(range(self.value))

    def __len__(self):
        return self.value

    def __contains__(self, item):
        return item in range(self.value)

    def __call__(self, *args, **kwargs):
        raise TypeError("'Short' object is not callable")
