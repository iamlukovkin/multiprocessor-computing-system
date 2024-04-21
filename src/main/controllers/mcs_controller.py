# src/main/controllers/mcs_controller.py
from src.main.models import MultiprocessorComputingSystem
from enum import Enum


class MCSController:
    __intencity: float
    __average_comlexity: float
    __average_time_to_excange: float
    __probablity: float
    __max_channels_count: int
    __counted_params: dict = {}

    def __init__(self, intencity: float, average_comlexity: float, average_time_to_excange: float,
                 probablity: float, max_channels_count: int) -> None:
        self.__intencity = intencity
        self.__average_comlexity = average_comlexity
        self.__average_time_to_excange = average_time_to_excange
        self.__probablity = probablity
        self.__max_channels_count = max_channels_count

    def get_dependency_queue_length(self) -> dict[int, float]:
        """
        Метод, возвращающий зависимость между количеством каналов и длиной очереди
        :return: dict[int, float] - словарь, в котором ключ - количество каналов, а значение - длина очереди
        """
        result: dict[int, float] = {}
        for channels_count in range(1, self.__max_channels_count + 1):
            result[channels_count] = self.__get_params()[channels_count][self.__Params.QUEUE_LENGTH]

        return result

    def get_dependency_minimal_time_for_service(self) -> dict[int, float]:
        """
        Метод, возвращающий зависимость между количеством каналов и минимального времени обслуживания
        :return: dict[int, float] - словарь, в котором ключ - количество каналов,
        а значение - минимальное время обслуживания
        """
        result: dict[int, float] = {}

        for channels_count in range(1, self.__max_channels_count + 1):
            result[channels_count] = self.__get_params()[channels_count][self.__Params.MINIMAL_TIME_FOR_SERVICE]

        return result

    def get_dependency_average_waiting_time(self) -> dict[int, float]:
        """
        Метод, возвращающий зависимость между количеством каналов и средней длине ожидания
        :return: dict[int, float] - словарь, в котором ключ - количество каналов,
        а значение - среднее время ожидания
        """
        result: dict[int, float] = {}

        for channels_count in range(1, self.__max_channels_count + 1):
            result[channels_count] = self.__get_params()[channels_count][self.__Params.AVERAGE_WAITING_TIME]

        return result

    def get_dependency_average_time_of_stay(self) -> dict[int, float]:
        """
        Метод, возвращающий зависимость между количеством каналов и средней длине пребывания заявок в системе
        :return:  dict[int, float] - словарь, в котором ключ - количество каналов,
        а значение - среднее время пребывания заявок в системе
        """
        result: dict[int, float] = {}

        for channels_count in range(1, self.__max_channels_count + 1):
            result[channels_count] = self.__get_params()[channels_count][self.__Params.AVERAGE_TIME_OF_STAY]
        return result

    def get_dependency_perfomance(self) -> dict[int, float]:
        """
        Метод, возвращающий зависимость между количеством каналов и производительности
        :return: dict[int, float] - словарь, в котором ключ - количество каналов,
        а значение - производительность
        """
        result: dict[int, float] = {}

        for channels_count in range(1, self.__max_channels_count + 1):
            result[channels_count] = self.__get_params()[channels_count][self.__Params.PERFORMANCE]

        return result

    def get_dependency_cpu_load(self) -> dict[int, float]:
        """
        Метод, возвращающий зависимость между количеством каналов и загруженности процессора
        :return: dict[int, float] - словарь, в котором ключ - количество каналов,
        а значение - загруженность процессора
        """
        result: dict[int, float] = {}

        for channels_count in range(1, self.__max_channels_count + 1):
            result[channels_count] = self.__get_params()[channels_count][self.__Params.CPU_LOAD]

        return result

    def __get_mcs(self, channels: int) -> MultiprocessorComputingSystem:
        return MultiprocessorComputingSystem(
            self.__intencity, self.__average_comlexity,
            self.__average_time_to_excange, self.__probablity,
            channels
        )

    class __Params(Enum):
        PERFORMANCE = 0
        CPU_LOAD = 1
        QUEUE_LENGTH = 2
        MINIMAL_TIME_FOR_SERVICE = 3
        AVERAGE_WAITING_TIME = 4
        AVERAGE_TIME_OF_STAY = 5

    def __count_params(self) -> None:
        for channels_count in range(1, self.__max_channels_count + 1):
            mcs: MultiprocessorComputingSystem = self.__get_mcs(channels_count)
            self.__counted_params[channels_count] = {
                self.__Params.PERFORMANCE: mcs.get_perfomance(),
                self.__Params.CPU_LOAD: mcs.get_cpu_load(),
                self.__Params.QUEUE_LENGTH: mcs.get_average_queue_length(),
                self.__Params.MINIMAL_TIME_FOR_SERVICE: mcs.get_service_of_any_request(),
                self.__Params.AVERAGE_WAITING_TIME: mcs.get_average_waiting_time(),
                self.__Params.AVERAGE_TIME_OF_STAY: mcs.get_average_time_of_stay()
            }
            print(mcs.__repr__())

    def __get_params(self) -> dict[int, dict[__Params, float]]:
        if len(self.__counted_params) == 0:
            self.__count_params()
        return self.__counted_params
