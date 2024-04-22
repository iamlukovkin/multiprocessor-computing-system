from abc import ABC
from abc import abstractmethod


class Singleton(ABC):
    __instance = None

    @abstractmethod
    def __init__(self) -> None:
        pass

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance
