from _typeshed import Self
from abc import ABC, abstractmethod

class Car(ABC):
    """Abstract class definition for Car model"""
    @abstractmethod
    def start(self):
        """Abstract method definition"""
        pass

    @abstractmethod
    def run(self):
        """Abstract run method"""
        pass

    @abstractmethod
    def stop(self):
        """Abstract stop method"""
        pass


class TeslaCar(Car):

    def __init__(self, name: str) -> None:
        self._name = name;

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @name.deleter
    def name(self) -> None:
        del self._name

    def start(self):
        return super().start()

    def run(self):
        return super().run()

    def stop(self):
        return super().stop()


class Jeep(Car):
    pass


class BMW(Car):
    pass