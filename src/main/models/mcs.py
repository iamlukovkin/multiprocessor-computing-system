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

    __service_of_any_request = 0

    def __init__(self, incoming_intencity: float, average_comlexity: float,
                 average_time_to_excange: float, probablity: float, channels_count: int = 1) -> None:
        self.__incoming_intencity = incoming_intencity
        self.__average_comlexity = average_comlexity * 1e3
        self.__average_time_to_excange = average_time_to_excange
        self.__probablity = probablity
        self.__channels_count = channels_count
        self.__get_required_perfomance()

    def __str__(self) -> str:
        return f"MultiprocessorComputingSystem(\n" \
               f"\tincoming_intencity={self.get_incoming_intencity()},\n" \
               f"\taverage_comlexity={self.get_average_comlexity()},\n" \
               f"\tchannels_count={self.get_channels_count()},\n" \
               f"\taverage_time_to_excange={self.get_average_time_to_excange()},\n" \
               f"\tprobablity={self.get_probablity()}\n"

    def __repr__(self) -> str:
        return f"MultiprocessorComputingSystem(\n" \
               f"\tperfomance={self.get_perfomance()}\n)" \
               f"\tcpu_load={self.get_cpu_load():.3f},\n" \
               f"\tservice_of_any_request={self.get_service_of_any_request():.6f},\n" \
               f"\taverage_queue_length={self.get_average_queue_length():6f},\n" \
               f"\taverage_waiting_time={self.get_average_waiting_time():.6f},\n" \
               f"\taverage_time_of_stay={self.get_average_time_of_stay():.6f}\n)"

    def get_cpu_load(self) -> float:
        """
        Метод, вычисляющий загрузку процессора
        """
        return self.get_service_of_any_request() * self.__incoming_intencity / self.__channels_count

    def get_service_of_any_request(self) -> float:
        """
        Метод, вычисляющий время обслуживания любой заявки
        :return: float - время обслуживания любой заявки
        """
        return self.__average_comlexity / self.__perfomance

    def get_average_queue_length(self) -> float:
        """
        Метод, вычисляющий среднюю длину очереди
        :return: float - средняя длина очереди
        """
        average_queue_length: float

        numenator: float = (self.__channels_count ** (self.__channels_count - 1)) * (
                self.get_cpu_load() ** (self.__channels_count + 1)
        )
        denominator: float = math.factorial(self.__channels_count - 1) * (1 - self.get_cpu_load()) ** 2
        try:
            average_queue_length = numenator / denominator * self.__probablity
        except ZeroDivisionError:
            average_queue_length = math.inf

        return average_queue_length

    def get_average_waiting_time(self) -> float:
        """
        Метод, вычисляющий среднее время ожидания заявок
        :return: float - среднее время ожидания заявок
        """
        average_waiting_time: float

        numenator: float = \
            self.get_service_of_any_request() * (self.__channels_count ** (self.__channels_count - 1)) * (
                    self.get_cpu_load() ** self.__channels_count)
        denominator: float = math.factorial(self.__channels_count) * ((1 - self.get_cpu_load()) ** 2)
        average_waiting_time = numenator / denominator * self.__probablity

        return average_waiting_time

    def get_average_time_of_stay(self) -> float:
        """
        Метод, вычисляющий среднее время пребывания зявок в системе
        :return: float - среднее время пребывания зявок в системе
        """
        return self.get_average_waiting_time() + self.get_service_of_any_request()

    def get_perfomance(self) -> float:
        """
        Метод, вычисляющий производительность процессора
        :return: float - производительность процессора
        """
        if self.__perfomance == 0:
            self.__perfomance = self.__get_required_perfomance()
        return self.__perfomance

    def get_incoming_intencity(self) -> float:
        """
        Метод, возвращающий интенсивность входящего потока
        :return: float - интенсивность входящего потока
        """
        return self.__incoming_intencity

    def get_average_comlexity(self) -> float:
        """
        Метод, возвращающий среднюю трудоемкость алгоритмов
        :return: float - среднюю трудоемкость алгоритмов
        """
        return self.__average_comlexity

    def get_channels_count(self) -> int:
        """
        Метод, возвращающий количество каналов
        :return: int - количество каналов
        """
        return self.__channels_count

    def get_average_time_to_excange(self) -> float:
        """
        Метод, возвращающий среднее время обмена
        :return: float - среднее время обмена
        """
        return self.__average_time_to_excange

    def get_probablity(self) -> float:
        """
        Метод, возвращающий вероятность простоя процессора
        :return: float - вероятность простоя процессора
        """
        return self.__probablity

    def __get_required_perfomance(self) -> float:
        """
        Метод, вычисляющий необходимую производительность процессора
        :return: float - необходимую производительность процессора
        """
        # while self.__incoming_intencity * self.__average_comlexity >= self.__perfomance:
        while self.__incoming_intencity * self.__average_comlexity >= self.__channels_count * self.__perfomance:
            self.__perfomance += 1

        while not self.__validate_perfomance():
            self.__perfomance += 1

        return self.__perfomance

    def __validate_perfomance(self) -> bool:
        is_cpu_bound_task: bool = self.__incoming_intencity * self.__average_comlexity \
                                  < self.__channels_count * self.__perfomance
        is__time_of_stay_bound_task: bool = self.get_average_time_of_stay() < self.__average_time_to_excange

        return is_cpu_bound_task & is__time_of_stay_bound_task
