import functools
"""
Prefer class decorators over metaclass
"""

def my_class_decorator(cls):
    """A basic class decorator"""
    for name, attr in vars(cls).items():
        print(f'{name}, {attr}')

def invariant(predicate):
    def invariant_checking_class_decorator(cls):
        method_names = [name for name, attr in vars(cls).items() if callable(attr)]
        for name in method_names:
            _wrap_method_with_invariant_checking_proxy(cls, name, predicate)
        return cls
    return invariant_checking_class_decorator

def _wrap_method_with_invariant_checking_proxy(cls, name, predicate):
    method = getattr(cls, name)
    assert callable(method)
    @functools.wraps(method)
    def invariant_checking_method_decorator(self, *args, **kwargs):
        result = method(self, *args, **kwargs)
        if not predicate(self):
            raise RuntimeError("Class invariant {!r} violated for {!r}".format(predicate.__doc__, self))
        return result
    setattr(cls, name, invariant_checking_method_decorator)


def not_below_absolute_zero(temperature):
    return temperature.kelvin >= 0


# Using the invariant decorator needs a function to validate its value, this is quite different
# from a functional decorator.
@invariant(not_below_absolute_zero)
class Temperature:
    def __init__(self, kelvin) -> None:
        self._kelvin = kelvin

    @property
    def kelvin(self):
        return self._kelvin

    @kelvin.setter
    def kelvin(self, kelvin):
        self._kelvin = kelvin


if __name__ == '__main__':
    temp = Temperature(-1.0)