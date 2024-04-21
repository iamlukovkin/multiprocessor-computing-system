from src.main.controllers import MCSController
from src.main.controllers import GraphicsController


def main() -> None:
    intencity: float = 2.5
    average_comlexity: float = 15
    average_time_to_excange: float = 0.15
    probablity: float = 0.4
    channels_count: int = 4

    controller: MCSController = MCSController(
        intencity, average_comlexity, average_time_to_excange, probablity, channels_count
    )

    average_time_of_stay: dict[int, float] = controller.get_dependency_average_time_of_stay()
    average_waiting_time: dict[int, float] = controller.get_dependency_average_waiting_time()
    queue_length_dependency: dict[int, float] = controller.get_dependency_queue_length()
    performance: dict[int, float] = controller.get_dependency_perfomance()
    cpu_load: dict[int, float] = controller.get_dependency_cpu_load()

    GraphicsController.make_average_time_of_stay_plot(average_time_of_stay)
    GraphicsController.make_average_waiting_time_plot(average_waiting_time)
    GraphicsController.make_queue_length_plot(queue_length_dependency)
    GraphicsController.make_performance_plot(performance)
    GraphicsController.make_cpu_load_plot(cpu_load)
    GraphicsController.make_performance_plot(performance)


if __name__ == "__main__":
    raise SystemError("This file should not be run directly")
