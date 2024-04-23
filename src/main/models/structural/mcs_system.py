from src.main.models.structural.mcs_individual import IndividualMCS


class SystemMCS:
    __mcs_individuals: list[IndividualMCS] = []
    __channels: int

    def __init__(self, invidiuals: list, channels: int) -> None:
        self.__mcs_individuals = invidiuals
        self.__channels = channels

    def get_mcs_list(self) -> list[IndividualMCS]:
        return self.__mcs_individuals

    def get_thread_intencity(self) -> float:
        return sum(individual.get_intencity() for individual in self.__mcs_individuals[0:self.__channels])

    def get_average_time_waiting_requests(self) -> float:
        result: float = 0
        for individual in self.__mcs_individuals[0:self.__channels]:
            result += individual.get_average_time_waiting_requests() * self.get_intencity_dependence(individual)
        return result

    def get_average_cpu_load(self) -> float:
        result: float = 0
        for individual in self.__mcs_individuals[0:self.__channels]:
            result += individual.get_cpu_load()
        return result / self.__channels

    def get_average_requests_time(self) -> float:
        result: float = 0
        for individual in self.__mcs_individuals[0:self.__channels]:
            result += individual.get_average_time_of_request() * self.get_intencity_dependence(individual)
        return result

    def get_average_queue_length(self) -> float:
        result: float = 0
        for individual in self.__mcs_individuals[0:self.__channels]:
            result += individual.get_average_request_count() * self.get_intencity_dependence(individual)
        return result

    def get_intencity_dependence(self, individual: IndividualMCS) -> float:
        return individual.get_intencity() / self.get_thread_intencity()
