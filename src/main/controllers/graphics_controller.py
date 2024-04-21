# src/main/controllers/graphics_controller.py
from src.main.models import GraphicsMaker


class GraphicsController:
    """
    Контроллер для работы с графикой
    """

    @staticmethod
    def make_average_time_of_stay_plot(average_time_of_stay: dict[int, float]) -> None:
        GraphicsMaker.make_plot(
            data=average_time_of_stay,
            x_name='Количество каналов',
            y_name='Среднее время пребывания заявок в системе',
            title='Зависимость среднего времени пребывания заявок в системе от количества каналов'
        )

    @staticmethod
    def make_average_waiting_time_plot(average_waiting_time: dict[int, float]) -> None:
        GraphicsMaker.make_plot(
            data=average_waiting_time,
            x_name='Количество каналов',
            y_name='Среднее время ожидания',
            title='Зависимость среднего времени ожидания от количества каналов'
        )

    @staticmethod
    def make_queue_length_plot(queue_length_dependency: dict[int, float]) -> None:
        GraphicsMaker.make_plot(
            data=queue_length_dependency,
            x_name='Количество каналов',
            y_name='Длина очереди',
            title='Зависимость длины очереди от количества каналов'
        )

    @staticmethod
    def make_performance_plot(performance_dependency: dict[int, float]) -> None:
        GraphicsMaker.make_plot(
            data=performance_dependency,
            x_name='Количество каналов',
            y_name='Параметр',
            title='Зависимость производительности от количества каналов'
        )

    @staticmethod
    def make_cpu_load_plot(cpu_load_dependency: dict[int, float]) -> None:
        GraphicsMaker.make_plot(
            data=cpu_load_dependency,
            x_name='Количество каналов',
            y_name='Загруженность процессора',
            title='Зависимость загруженности процессора от количества каналов'
        )
