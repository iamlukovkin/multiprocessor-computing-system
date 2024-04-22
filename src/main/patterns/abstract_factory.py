from src.main.patterns.singleton import Singleton
from abc import abstractmethod


class AbstractFactory(Singleton):
    @abstractmethod
    def create(self, *args, **kwargs):
        pass
