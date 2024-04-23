# src/application.py
from src.main.controllers import MCSController
from src.main.controllers import PlotsController
from src.main.controllers import MCSDataController
from src.main.controllers import SystemController
from src.main.controllers import TablesController


class Application:
    __mcs_controller: MCSController = None
    __plots_controller: PlotsController = None

    @staticmethod
    def lab4() -> None:
        intensity: float = 2.5
        complexity: float = 15
        channels: int = 6
        probability: float = 0.15

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

    @staticmethod
    def lab5() -> None:
        intencities: list = [1.5, 2.5, 3.5, 4.0, 5.0, 7.1, 8.2, 5.1, 6.0, 7.3]
        complexities: list = [27, 28, 32, 5, 10, 30, 25, 20, 15, 10]
        channels: int = 6

        start_perfomance: int = 200_000
        end_perfomance: int = 1_000_000
        count_perfomances: int = 10
        step: int = (end_perfomance - start_perfomance) // count_perfomances

        perfomances = [value for value in range(start_perfomance, end_perfomance, step)]
        controller: SystemController = SystemController(intencities, complexities, channels, perfomances)
        data: dict = controller.get_minimal_perfomance_characteristics()
        TablesController.save_minimal_perfomance_characteristics(data)
        data: dict = controller.calculate()
        MCSDataController.display(data)
