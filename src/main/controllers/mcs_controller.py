# src/main/controllers/mcs_controller.py
from src.main.models.creational import MCSFabric
from src.main.models.structural import MCSModel
from src.main.models.structural import MCSParametres


class MCSController:
    __intensity: float
    __complexity: float
    __channels: int
    __probability: float

    __mcs_model: MCSModel = None

    def __init__(self, intensity: float, complexity: float, probability: float) -> None:
        self.__intensity = intensity
        self.__complexity = complexity
        self.__probability = probability

    @classmethod
    def get_perfomances(cls, start: int, end: int, count: int) -> list:
        __start: int = start * 1000
        __end: int = end * 1000
        __step: int = (__end - __start) // count
        return list(range(__start, __end, __step))

    def calculate(self, max_channels: int, perfomances: list) -> dict:
        data: dict = {}
        for channels_count in range(1, max_channels + 1):
            data[channels_count] = {}
            for perfomance in perfomances:
                data[channels_count][perfomance] = {}
                parametres = self.calculate_parameters(channels_count, perfomance)
                data[channels_count][perfomance] = {
                    MCSParametres.AVERAGE_WAITING_TIME: parametres[0],
                    MCSParametres.AVERAGE_QUEUE_LENGTH: parametres[1],
                    MCSParametres.AVERAGE_TIME_OF_REQUEST: parametres[2]
                }
        return data

    def calculate_parameters(self, channels_count: int, perfomance: float) -> tuple:
        average_waiting_time: float = self.get_average_waiting_time(
            channels_count, perfomance)
        average_queue_length: float = self.get_average_queue_length(
            channels_count, perfomance)
        average_time_of_request: float = self.get_average_time_of_request(
            channels_count, perfomance)
        return average_waiting_time, average_queue_length, average_time_of_request

    def get_average_waiting_time(self, channels: int, perfomance: float) -> float:
        mcs_model: MCSModel = self.__get_mcs_model(channels, perfomance)
        return mcs_model.get_average_waiting_time()

    def get_average_queue_length(self, channels: int, perfomance: float) -> float:
        mcs_model: MCSModel = self.__get_mcs_model(channels, perfomance)
        return mcs_model.get_average_queue_length()

    def get_average_time_of_request(self, channels: int, perfomance: float) -> float:
        mcs_model: MCSModel = self.__get_mcs_model(channels, perfomance)
        return mcs_model.get_average_time_of_request()

    def get_cpu_load(self, channels: int, perfomance: float) -> float:
        mcs_model: MCSModel = self.__get_mcs_model(channels, perfomance)
        return mcs_model.get_cpu_load()

    def __get_mcs_model(self, channels: int, perfomance: float) -> MCSModel:
        mcs_fabric: MCSFabric = MCSFabric.get_instance()
        return mcs_fabric.create(self.__intensity, self.__complexity, channels, self.__probability, perfomance)

    def get_minimal_perfomance(self):
        return self.__intensity * self.__complexity * 1e3

    def get_minimal_perfomance_characteristics(self):
        mcs_model: MCSModel = self.__get_mcs_model(1, self.get_minimal_perfomance())
        return {
            MCSParametres.SINGLE_PROCESSOR_PERFOMANCE:
                mcs_model.get_single_processor_perfomance(),

            MCSParametres.SERVICE_TIME:
                mcs_model.get_service_time(),

            MCSParametres.CPU_LOAD: mcs_model.get_cpu_load(),

            MCSParametres.AVERAGE_QUEUE_LENGTH:
                mcs_model.get_average_queue_length(),

            MCSParametres.AVERAGE_WAITING_TIME:
                mcs_model.get_average_waiting_time(),

            MCSParametres.AVERAGE_TIME_OF_REQUEST:
                mcs_model.get_average_time_of_request()
        }
