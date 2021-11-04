
from typing import AbstractSet, Iterable, Iterator, Sequence

from abc import ABCMeta


def check_sub_class():
    print(issubclass(list, object))
    print(issubclass(list, Sequence))
    print(issubclass(list, Iterable))


class Sword(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, sub):
        return ((hasattr(sub, 'swipe') and callable(sub.swipe) 
            and 
            hasattr(sub, 'sharpen') and callable(sub.sharpen)) 
            or NotImplemented)

    def thrust(self):
        print('Thrusting')


class BoardSword:
    def swipe(self):
        print('Swiping everything!')

    def sharpen(self):
        print('Shink!')


class SamuraiSword:
    def swipe(self):
        print('Slice')

    def sharpen(self):
        print('Shink')



class Text(metaclass=ABCMeta):
    pass




if __name__ == '__main__':
    check_sub_class()
    boardSword = BoardSword()
    samuraiSword = SamuraiSword()
    print(issubclass(BoardSword, Sword))
    print(isinstance(boardSword, Sword))
    Text.register(str)
    print(issubclass(str, Text))
    print(isinstance('Is this a Text', Text))