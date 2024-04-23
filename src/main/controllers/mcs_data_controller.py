# src/main/controllers/mcs_data_controller.py
from src.main.controllers import PlotsController
from src.main.views import PlotsView
from src.main.controllers.tables_controller import TablesController
from src.main.controllers.mcs_controller import MCSController


class MCSDataController:
    @staticmethod
    def display_average_waiting_time(data: dict) -> None:
        converted_data: dict = PlotsController.convert_average_waiting_time(data)
        TablesController.save_waiting_time(converted_data)
        PlotsView.display_average_waiting_time(converted_data)

    @staticmethod
    def display_average_time_of_request(data: dict) -> None:
        converted_data: dict = PlotsController.convert_average_time_of_request(data)
        TablesController.save_average_time_of_request(converted_data)
        PlotsView.display_average_time_of_request(converted_data)

    @staticmethod
    def display_average_queue_length(data: dict) -> None:
        converted_data: dict = PlotsController.convert_average_queue_length(data)
        TablesController.save_average_queue_length(converted_data)
        PlotsView.display_average_queue_length(converted_data)

    @staticmethod
    def display(data: dict) -> None:
        MCSDataController.display_average_waiting_time(data)
        MCSDataController.display_average_time_of_request(data)
        MCSDataController.display_average_queue_length(data)
        MCSDataController.display_cpu_load(data)

    @staticmethod
    def collect_minimal_perfomance_data(controller: MCSController) -> None:
        data: dict = controller.get_minimal_perfomance_characteristics()
        TablesController.save_minimal_perfomance_characteristics(data)

    @staticmethod
    def display_cpu_load(data: dict) -> None:
        converted_data: dict = PlotsController.convert_cpu_load(data)
        PlotsView.display_cpu_load(converted_data)

    @staticmethod
    def display_system(data: dict, channels: int, perfomances: list) -> None:
        converted_data: list = PlotsController.conver_system_data(data, channels, perfomances)
        PlotsView.display_average_queue_length(converted_data[0])
        PlotsView.display_average_waiting_time(converted_data[1])
        PlotsView.display_average_time_of_request(converted_data[2])
