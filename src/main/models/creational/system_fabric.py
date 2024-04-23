from src.main.patterns.abstract_factory import AbstractFactory
from src.main.models.structural.mcs_system import SystemMCS
from src.main.models.structural.mcs_individual import IndividualMCS


class SystemMCSFabric(AbstractFactory):
    def __init__(self):
        pass

    def create(self, intencities: list, complexitites: list, channels: int, perfomance: float) -> SystemMCS:
        individual_mcs: list[IndividualMCS] = []
        for index in range(0, len(intencities)):
            individual_mcs.append(IndividualMCS(
                intencity=intencities[index],
                complexity=complexitites[index],
                perfomance=perfomance
            ))
        return SystemMCS(individual_mcs, channels)
