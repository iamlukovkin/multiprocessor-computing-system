# src/main/models/structural/mcs_individual
import math


class IndividualMCS:
    __intensity: float
    __complexity: float
    __perfomance: float

    def __init__(self, intencity: float, complexity: float, perfomance: float) -> None:
        self.__intensity = intencity
        self.__complexity = complexity * 1e3
        self.__perfomance = perfomance

    def get_complexity(self) -> float:
        return self.__complexity

    def get_perfomance(self) -> float:
        return self.__perfomance

    def get_intencity(self) -> float:
        return self.__intensity

    def get_cpu_load(self) -> float:
        cpu_load: float = self.get_intencity() * self.get_service_time()
        if cpu_load >= 1:
            return 1
        if cpu_load < 0:
            return 0
        return cpu_load

    def get_service_time(self) -> float:
        return self.get_complexity() / self.get_perfomance()

    def get_average_time_waiting_requests(self):
        cpu_load: float = self.get_cpu_load()
        try:
            return (cpu_load / math.fabs(1 - cpu_load)) * self.get_service_time()
        except ZeroDivisionError:
            return 0

    def get_average_time_of_request(self) -> float:
        try:
            return math.fabs(1 / (1 - self.get_cpu_load())) * self.get_service_time()
        except ZeroDivisionError:
            return 0

    def get_average_request_count(self) -> float:
        cpu_load: float = self.get_cpu_load()
        try:
            return (cpu_load ** 2) / math.fabs(1 - cpu_load)
        except ZeroDivisionError:
            return 0
