# src/main/models/structural/plots_controller.py
from src.main.models.structural import MCSParametres


class PlotsController:
    @staticmethod
    def __convert_data(data: dict, parametres: MCSParametres) -> dict:
        result: dict = {}
        for channels_count in data:
            for perfomance in data[channels_count]:
                if perfomance not in result:
                    result[perfomance] = {}
                result[perfomance][channels_count] = \
                    data[channels_count][perfomance][parametres]
        return result

    @staticmethod
    def convert_average_waiting_time(data: dict) -> dict:
        return PlotsController.__convert_data(data, MCSParametres.AVERAGE_WAITING_TIME)

    @staticmethod
    def convert_average_time_of_request(data: dict) -> dict:
        return PlotsController.__convert_data(data, MCSParametres.AVERAGE_TIME_OF_REQUEST)

    @staticmethod
    def convert_average_queue_length(data: dict) -> dict:
        return PlotsController.__convert_data(data, MCSParametres.AVERAGE_QUEUE_LENGTH)
    
    @staticmethod
    def convert_cpu_load(data: dict) -> dict:
        return PlotsController.__convert_data(data, MCSParametres.CPU_LOAD)

    @staticmethod
    def conver_system_data(data: dict, channels: int, perfomances: list) -> list:
        result: dict = {
            MCSParametres.AVERAGE_QUEUE_LENGTH: {},
            MCSParametres.AVERAGE_WAITING_TIME: {},
            MCSParametres.AVERAGE_TIME_OF_REQUEST: {}
        }
        for plot in result.keys():
            for perfomance in perfomances:
                result[plot][perfomance] = {}
                for channel in range(1, channels + 1):
                    result[plot][perfomance][channel] = data[channel][perfomance][plot]
        return [value for value in result.values()]
