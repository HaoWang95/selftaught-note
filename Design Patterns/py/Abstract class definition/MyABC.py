import abc


class MyABC(abc.ABC):
    """Abstract Base Class definition"""
    
    @abc.abstractmethod
    def do_something(self, value):
        """Required method"""

    @abc.abstractproperty
    def some_property(self):
        """Required property"""


class ABClass(MyABC):
    """Implementation of the abstract base class"""
    def __init__(self, value=None) -> None:
        super().__init__()
        self._prop = value
    
    def do_something(self, value):
        """Implementation of the abstract method"""
        self._prop += value

    @property
    def some_property(self):
        """Implementation of abstract property"""
        return self._prop
    
    @some_property.setter
    def some_property(self, value):
        self._prop = value
        
if __name__ == '__main__':
    instance = ABClass(1)
    print(instance.__dict__.items())
    print(instance.some_property)
    instance.some_property = 2
    print(instance.some_property)