# src/main/controllers/mcs_controller.py
from src.models import MultiprocessorComputingSystem
from enum import Enum


class MCSController:
    __incoming_intencity: float
    __average_comlexity: float
    __average_time_to_excange: float
    __probablity: float
    __max_channels_count: int
    __counted_params: dict = {}

    def __init__(self, intencity: float, average_comlexity: float, average_time_to_excange: float,
                 probablity: float, max_channels_count: int) -> None:
        self.__incoming_intencity = intencity
        self.__average_comlexity = average_comlexity
        self.__average_time_to_excange = average_time_to_excange
        self.__probablity = probablity
        self.__max_channels_count = max_channels_count

    def get_dependency_queue_length(self):
        """
        Метод, возвращающий зависимость между количеством каналов и длиной очереди
        :return: dict[int, float] - словарь, в котором ключ - количество каналов, а значение - длина очереди
        """
        result = {}
        for channels_count in range(1, self.__max_channels_count + 1):
            result[channels_count] = self.__get_params()[channels_count][self.__Params.QUEUE_LENGTH]

        return result

    def get_dependency_average_waiting_time(self):
        """
        Метод, возвращающий зависимость между количеством каналов и средней длине ожидания
        :return: dict[int, float] - словарь, в котором ключ - количество каналов,
        а значение - среднее время ожидания
        """
        result = {}

        for channels_count in range(1, self.__max_channels_count + 1):
            result[channels_count] = self.__get_params()[channels_count][self.__Params.AVERAGE_WAITING_TIME]

        return result

    def get_dependency_average_time_of_stay(self):
        """
        Метод, возвращающий зависимость между количеством каналов и средней длине пребывания заявок в системе
        :return:  dict[int, float] - словарь, в котором ключ - количество каналов,
        а значение - среднее время пребывания заявок в системе
        """
        result = {}
        for channels_count in range(1, self.__max_channels_count + 1):
            result[channels_count] = self.__get_params()[channels_count][self.__Params.AVERAGE_TIME_OF_STAY]
        return result

    def calculate_minimal_perfomance(self):
        result: list = []
        for channels_count in range(1, self.__max_channels_count + 1):
            mcs_for_count: MultiprocessorComputingSystem = self.__get_mcs(channels_count)
            result.append(mcs_for_count.get_perfomance())
        return min(result)

    def __get_mcs(self, channels: int, perfomance: float = None) -> MultiprocessorComputingSystem:
        return MultiprocessorComputingSystem(
            incoming_intencity=self.__incoming_intencity,
            average_comlexity=self.__average_comlexity,
            channels_count=channels,
            average_time_to_excange=self.__average_time_to_excange,
            probablity=self.__probablity,
            perfomance=perfomance
        )

    class __Params(Enum):
        PERFORMANCE = 0
        CPU_LOAD = 1
        QUEUE_LENGTH = 2
        MINIMAL_TIME_FOR_SERVICE = 3
        AVERAGE_WAITING_TIME = 4
        AVERAGE_TIME_OF_STAY = 5

    def __count_params(self) -> None:
        calculated_perfomance = self.calculate_minimal_perfomance()
        for channels_count in range(1, self.__max_channels_count + 1):
            mcs: MultiprocessorComputingSystem = self.__get_mcs(channels_count, calculated_perfomance)
            self.__counted_params[channels_count] = {
                self.__Params.QUEUE_LENGTH: mcs.get_average_queue_length(),
                self.__Params.AVERAGE_WAITING_TIME: mcs.get_average_waiting_time(),
                self.__Params.AVERAGE_TIME_OF_STAY: mcs.get_average_time_of_stay()
            }

    def __get_params(self):
        if len(self.__counted_params) == 0:
            self.__count_params()
        return self.__counted_params
