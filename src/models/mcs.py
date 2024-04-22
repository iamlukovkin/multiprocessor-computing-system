# src/main/models/mcs.py
import math


class MultiprocessorComputingSystem:
    """
    Класс, описывающий мультипроцессорную систему

    Атрибуты:
        __incoming_intencity: float - интенсивность входящего потока
        __average_comlexity: float - средняя сложность входящей задачи
        __channels_count: int - количество каналов
        __average_time_to_excange: float - среднее время обмена
        __probablity: float - вероятность
    """
    __incoming_intencity: float
    __average_comlexity: float
    __channels_count: int
    __average_time_to_excange: float
    __probablity: float
    __perfomance: float = 0

    __approximate_perfomance: float = 0

    def __init__(self, incoming_intencity: float, average_comlexity: float, channels_count: int,
                 average_time_to_excange: float, probablity: float, perfomance: float | None = None) -> None:
        self.__incoming_intencity = incoming_intencity
        self.__average_comlexity = average_comlexity * 1e3
        self.__average_time_to_excange = average_time_to_excange
        self.__probablity = probablity
        self.__channels_count = channels_count
        if perfomance is not None:
            self.__perfomance = perfomance
        else:
            self.calculate_perfomance()

    def calculate_perfomance(self):
        self.get_perfomance()
        self.get_average_time_of_stay()

    def __str__(self) -> str:
        return f"MultiprocessorComputingSystem(\n" \
               f"\tincoming_intencity={self.get_incoming_intencity()},\n" \
               f"\taverage_comlexity={self.get_average_comlexity()},\n" \
               f"\tchannels_count={self.get_channels_count()},\n" \
               f"\taverage_time_to_excange={self.get_average_time_to_excange()},\n" \
               f"\tprobablity={self.get_probablity()}\n"

    def get_incoming_intencity(self) -> float:
        return self.__incoming_intencity

    def get_average_comlexity(self) -> float:
        return self.__average_comlexity

    def get_channels_count(self) -> int:
        return self.__channels_count

    def get_average_time_to_excange(self) -> float:
        return self.__average_time_to_excange

    def get_probablity(self) -> float:
        return self.__probablity

    def __repr__(self) -> str:
        return f"MultiprocessorComputingSystem(\n" \
               f"\tperfomance={self.get_perfomance()}\n)" \
               f"\tcpu_load={self.get_cpu_load():.3f},\n" \
               f"\tservice_of_any_request={self.get_service_of_any_request():.6f},\n" \
               f"\taverage_queue_length={self.get_average_queue_length():6f},\n" \
               f"\taverage_waiting_time={self.get_average_waiting_time():.6f},\n" \
               f"\taverage_time_of_stay={self.get_average_time_of_stay():.6f}\n)"

    def get_service_of_any_request(self) -> float:
        """
        Метод, вычисляющий время обслуживания любой заявки
        :return: float - время обслуживания любой заявки
        """
        return self.__average_comlexity / self.get_perfomance()

    def get_perfomance(self) -> float:
        if self.__incoming_intencity * self.__average_comlexity <= self.__perfomance:
            return self.__perfomance
        while self.__incoming_intencity * self.__average_comlexity > self.__perfomance:
            self.__perfomance += 1

        return self.__perfomance

    def get_cpu_load(self) -> float:
        """
        Метод, вычисляющий загрузку процессора
        """
        while not (self.__incoming_intencity * self.__average_comlexity
                   < self.__channels_count * self.get_perfomance()):
            self.__perfomance += 1

        return (self.__incoming_intencity * self.__average_comlexity) / (
                self.__perfomance * self.__channels_count)

    def get_average_queue_length(self):
        """
        Метод, вычисляющий среднюю длину очереди
        :return: float - среднюю длину очереди
        """
        numenator: float = (self.__channels_count ** (self.__channels_count - 1)) * (
                self.get_cpu_load() ** (self.__channels_count + 1))
        denominator: float = math.factorial(self.__channels_count - 1) * math.pow(1 - self.get_cpu_load(), 2)
        return numenator / denominator * self.__probablity

    def get_average_waiting_time(self) -> float:
        """
        Метод, вычисляющий среднее время ожидания заявки
        :return: float - среднее время ожидания заявки
        """
        return self.get_average_queue_length() * self.get_service_of_any_request() \
            / self.__channels_count / self.get_cpu_load()

    def get_average_time_of_stay(self) -> float:
        """
        Метод, вычисляющий среднее время пребывания зявок в системе
        :return: float - среднее время пребывания зявок в системе
        """
        while self.get_average_waiting_time() + self.get_service_of_any_request() > self.__average_time_to_excange:
            self.__perfomance += 1
        return self.get_average_waiting_time() + self.get_service_of_any_request()
