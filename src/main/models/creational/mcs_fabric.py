from abc import ABC

from src.main.patterns.abstract_factory import AbstractFactory
from src.main.models.structural.mcs_model import MCSModel


class MCSFabric(AbstractFactory, ABC):
    def __init__(self):
        super().__init__()

    def create(self, intensity: float, complexity: float, channels: int,
               probability: float, perfomance: float) -> MCSModel:
        return MCSModel(intensity, complexity, channels, probability, perfomance)
