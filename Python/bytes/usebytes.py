import sys
from typing import Any, Type

def test_bitwise():
    num = b''
    print(sys.byteorder)


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def show(self):
        print(self.__sizeof__())

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.x}, {self.y})'


class Cord:
    """A cordination implementation"""
    def __new__(cls, **args):
        obj = super().__new__(cls, args)
        return obj

    def __init__(self, **cord) -> None:
        private_coords = {'_' + k: v for k, v in cord.items()}
        self.__dict__.update(private_coords)

    def __getattr__(self, name):
        try:
            return self.__dict__['_'+name]
        except KeyError:
            raise AttributeError('{!r} object has no attribute {!r}'.format(self.__class__, name))


    def __setattr__(self, name: str, value: Any) -> None:
        pass

    def __delattr__(self, name: str) -> None:
        pass

    def __repr__(self) -> str:
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join('{k}={v}'.format(
                k=k[1:], 
                v=self.__dict__[k])
                for k in self.__dict__.keys()))

class CountryContainer:
    """A container to store different countries"""
    def __init__(self, *data) -> None:
        self.__country_list = list(data)

    def __iter__(self):
        for c in self.__country_list:
            yield c


if __name__ == '__main__':
    p: Point = Point(1,2)
    print(p)
    p.show()
    cord: Cord = Cord(x=1, y=2, z=3)
    print(cord)
    print(dir(cord))
    print(cord.x, cord.y, cord.z)
    print(Cord.__class__.__dict__)
    print(Cord.__doc__)
    country = CountryContainer("USA","CN","AU","JNP","SKR","RU","GB")
    for c in country:
        print(c)