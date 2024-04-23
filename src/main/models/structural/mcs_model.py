# src/main/models/mcs_model.py
import math


class MCSModel:
    __intensity: float
    __complexity: float
    __channels: int
    __exchange_time: float
    __probability: float
    __single_processor_perfomance: float

    @classmethod
    def validate(cls, value: float) -> bool:
        return value > 0

    def __init__(self, intensity: float, complexity: float, channels: int,
                 probability: float, single_processor_perfomance: float) -> None:
        self.__intensity = intensity
        self.__complexity = complexity * 1e3
        self.__channels = channels
        self.__probability = probability
        self.__single_processor_perfomance = single_processor_perfomance

    def __str__(self):
        return f"MCSModel(\n" \
               f"\tintensity={self.get_intensity()},\n" \
               f"\tcomplexity={self.get_complexity()},\n" \
               f"\tchannels={self.get_channels()},\n" \
               f"\tprobability={self.get_probability()},\n" \
               f"\tsingle_processor_perfomance={self.get_single_processor_perfomance()}\n)"

    def __repr__(self):
        return f"MCSModel(\n" \
               f"\tavegare_queue_length={self.get_average_queue_length()},\n" \
               f"\tcpu_load={self.get_cpu_load()},\n" \
               f"\taverage_waiting_time={self.get_average_waiting_time()},\n" \
               f"\taverage_time_of_request={self.get_average_time_of_request()}\n)"

    def set_intensity(self, intensity: float) -> None:
        self.__intensity = intensity

    def get_intensity(self) -> float:
        return self.__intensity

    def set_complexity(self, complexity: float) -> None:
        self.__complexity = complexity

    def get_complexity(self) -> float:
        return self.__complexity

    def set_channels(self, channels: int) -> None:
        if channels <= 0:
            raise ValueError("Channels must be positive")
        self.__channels = channels

    def get_channels(self) -> int:
        return self.__channels

    def set_probability(self, probability: float) -> None:
        self.__probability = probability

    def get_probability(self) -> float:
        return self.__probability

    def set_single_processor_perfomance(self, single_processor_perfomance: float) -> None:
        self.__single_processor_perfomance = single_processor_perfomance

    def get_single_processor_perfomance(self) -> float:
        return self.__single_processor_perfomance

    def get_service_time(self) -> float:
        return self.__complexity / self.get_single_processor_perfomance()

    def get_perfomance(self) -> float:
        return self.get_single_processor_perfomance() * self.get_channels()

    def get_cpu_load(self) -> float:
        return self.get_intensity() * self.get_complexity() / \
            self.get_single_processor_perfomance() / self.get_channels()

    def get_average_queue_length(self) -> float:
        channels: int = self.get_channels()
        cpu_load: float = self.get_cpu_load()
        if cpu_load == 1:
            return math.inf
        return ((channels ** (channels - 1)) * (cpu_load ** (channels + 1))) \
            / (math.factorial(channels - 1) * ((1 - cpu_load) ** 2)) \
            * self.get_probability()

    def get_average_waiting_time(self) -> float:
        channels: int = self.get_channels()
        cpu_load: float = self.get_cpu_load()
        try:
            return ((self.get_service_time() * (channels ** (channels - 1)) * (cpu_load ** channels))
                    / (math.factorial(channels - 1) * ((1 - cpu_load) ** 2))
                    * self.get_probability())
        except ZeroDivisionError:
            return math.inf

    def get_average_time_of_request(self) -> float:
        return self.get_average_waiting_time() + self.get_service_time()
