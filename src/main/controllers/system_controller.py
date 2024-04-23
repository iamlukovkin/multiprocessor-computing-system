# src/main/controllers/system_controller.py
from src.main.models.creational import SystemMCSFabric
from src.main.models.structural import SystemMCS
from src.main.models.structural import MCSParametres


class SystemController:
    __intencities: list
    __complexities: list
    __channels: int
    __perfomances: list

    def __init__(self, intencities: list, complexities: list, channels: int, perfomances: list) -> None:
        self.__intencities = intencities
        self.__complexities = complexities
        self.__channels = channels
        self.__perfomances = perfomances

    def get_minimal_perfomance(self) -> float:
        return sum(self.__intencities[:self.__channels]) * sum(self.__complexities[:self.__channels]) * 1e3

    def get_minimal_perfomance_characteristics(self):
        perfomance: float = self.get_minimal_perfomance()
        mcs: SystemMCS = SystemMCSFabric.get_instance().create(
            self.__intencities, self.__complexities, self.__channels, perfomance)
        return {
            MCSParametres.SINGLE_PROCESSOR_PERFOMANCE: perfomance,

            MCSParametres.SERVICE_TIME:
                mcs.get_intencity_dependence(mcs.get_mcs_list()[0]),

            MCSParametres.CPU_LOAD: mcs.get_mcs_list()[0].get_cpu_load(),

            MCSParametres.AVERAGE_QUEUE_LENGTH:
                mcs.get_average_queue_length(),

            MCSParametres.AVERAGE_WAITING_TIME:
                mcs.get_average_time_waiting_requests(),

            MCSParametres.AVERAGE_TIME_OF_REQUEST:
                mcs.get_average_requests_time()
        }

    def calculate(self) -> dict:
        result: dict = {}
        for channels_count in range(1, self.__channels + 1):
            result[channels_count] = {}
            for perfomance in self.__perfomances:
                result[channels_count][perfomance] = {}
                system: SystemMCS = SystemMCSFabric.get_instance().create(
                    self.__intencities, self.__complexities, channels_count, perfomance)
                result[channels_count][perfomance] = {
                    MCSParametres.AVERAGE_QUEUE_LENGTH: system.get_average_queue_length(),
                    MCSParametres.AVERAGE_WAITING_TIME: system.get_average_time_waiting_requests(),
                    MCSParametres.AVERAGE_TIME_OF_REQUEST: system.get_average_requests_time(),
                    MCSParametres.CPU_LOAD: system.get_average_cpu_load()
                }
        return result
