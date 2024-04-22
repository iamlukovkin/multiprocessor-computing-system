# src/application.py
from src.main.controllers import MCSController
from src.main.controllers import PlotsController
from src.main.controllers import MCSDataController


class Application:
    __mcs_controller: MCSController = None
    __plots_controller: PlotsController = None

    @staticmethod
    def main() -> None:
        intensity: float = 0.5
        complexity: float = 18
        channels: int = 6
        probability: float = 0.55

        start_perfomance: int = 20
        end_perfomance: int = 120
        count_perfomances: int = 10

        Application.__mcs_controller = MCSController(intensity, complexity, probability)
        Application.__plots_controller = PlotsController()

        MCSDataController.collect_minimal_perfomance_data(Application.__mcs_controller)
        perfomances: list[float] = Application.__mcs_controller.get_perfomances(
            start_perfomance, end_perfomance, count_perfomances)
        data: dict = Application.__mcs_controller.calculate(channels, perfomances)
        MCSDataController.display(data)

