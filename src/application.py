from src.controllers import MCSController
from src.views import GraphicsView
from src.views import MCSView


class Application:
    __mcs_controller: MCSController

    @staticmethod
    def main() -> None:
        Application.setup_controller()
        Application.display_graphics()
        SystemExit(0)

    @staticmethod
    def setup_controller() -> None:
        intencity: float = 2.5
        average_comlexity: float = 15
        channels_count: int = 4
        average_time_to_excange: float = 0.15
        probablity: float = 0.4

        Application.__mcs_controller = MCSController(
            intencity, average_comlexity, average_time_to_excange, probablity, channels_count)

    @staticmethod
    def display_graphics() -> None:
        controller: MCSController = Application.__mcs_controller

        queue_length_dependency: dict[int, float] = controller.get_dependency_queue_length()
        GraphicsView.display_queue_length(queue_length_dependency)

        average_waiting_time: dict[int, float] = controller.get_dependency_average_waiting_time()
        GraphicsView.display_average_waiting_time(average_waiting_time)

        average_time_of_stay: dict[int, float] = controller.get_dependency_average_time_of_stay()
        GraphicsView.display_average_time_of_stay(average_time_of_stay)

        print(MCSView.display_minimal_perfomance(controller.calculate_minimal_perfomance()))
        return
