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
