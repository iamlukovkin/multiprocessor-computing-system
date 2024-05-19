# src/main/controllers/tables_controller.py
import pandas as pd
from src.main.models.structural.mcs_parametres import MCSParametres


class TablesController:
    def __init__(self):
        pass

    @staticmethod
    def save_data_to_xlsx(data: dict, save_path: str) -> None:
        path: str = 'res/tables/' + save_path
        df = pd.DataFrame(data)
        df.to_excel(path, index=False, startrow=1)

    @staticmethod
    def save_waiting_time(data: dict) -> None:
        result: dict = TablesController.prepare_data_for_save(data)
        TablesController.save_data_to_xlsx(result, 'waiting_time.xlsx')

    @staticmethod
    def save_average_queue_length(data: dict) -> None:
        result: dict = TablesController.prepare_data_for_save(data)
        TablesController.save_data_to_xlsx(result, 'average_queue_length.xlsx')

    @staticmethod
    def save_average_time_of_request(data: dict) -> None:
        result: dict = TablesController.prepare_data_for_save(data)
        TablesController.save_data_to_xlsx(result, 'average_time_of_request.xlsx')

    @staticmethod
    def prepare_data_for_save(data: dict) -> dict:
        result: dict = {}
        for perfomance in data:
            result[perfomance] = [data[perfomance][key] for key in data[perfomance].keys()]
        return result

    @staticmethod
    def save_minimal_perfomance_characteristics(data: dict) -> None:
        """
        Сохраняет данные о минимальной производительности в виде таблицы в xlsx
        :param data: словарь с характеристиками (из контроллера)
        :return: None
        """
        result: dict = {    # Формирование заголовков таблицы
            "Производительность процессора, оп/с": [data[MCSParametres.SINGLE_PROCESSOR_PERFOMANCE]],
            "Средняя нагрузка CPU, %": [data[MCSParametres.CPU_LOAD]],
            "Среднее время ожидания, с": [data[MCSParametres.AVERAGE_WAITING_TIME]],
            "Среднее время обработки запроса, с": [data[MCSParametres.AVERAGE_TIME_OF_REQUEST]],
            "Средняя длина очереди заявок, с": [data[MCSParametres.AVERAGE_QUEUE_LENGTH]],
            "Среднее время обслуживания одной заявки, с": [data[MCSParametres.SERVICE_TIME]]
        }
        TablesController.save_data_to_xlsx(result, 'minimal_perfomance_characteristics.xlsx')   # Сохранение
