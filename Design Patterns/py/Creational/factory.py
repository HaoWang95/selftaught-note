from _typeshed import Self
from abc import ABC, abstractmethod
from inspect import getmembers, isclass, isabstract


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

    def __init__(self, name: str=None) -> None:
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
        print(f'Tesla {self._name} is started.')

    def run(self):
        print(f'Tesla {self._name} is running')

    def stop(self):
        print(f'Tesla {self._name} is stopped')


class Jeep(Car):
    def __init__(self, name=None) -> None:
        self.name = name
    
    def run(self):
        print(f'Jeep {self.name} is running')

    def start(self):
        print(f'Jeep {self.name} is started')

    def stop(self):
        print(f'Jeep {self.name} is stopped')


class BMW(Car):
    def __init__(self, name) -> None:
        self.name = name

    def run(self):
        print(f'BWM {self.name} is running')

    def start(self):
        print(f'BWM {self.name} is started')

    def stop(self):
        print(f'BMW {self.name} is stopped')


class AbstractCarFactory(ABC):
    @abstractmethod
    def create_auto(self):
        pass


class TeslaFactory(AbstractCarFactory):
    def create_auto(self):
        self.tesla = tesla = TeslaCar(name="default")
        return tesla