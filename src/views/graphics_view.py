# src/main/views/graphics_view.py
from src.models import GraphicsMaker


class GraphicsView:
    @staticmethod
    def display_average_time_of_stay(average_time_of_stay: dict[int, float]) -> None:
        GraphicsMaker.make_plot(
            data=average_time_of_stay,
            x_name='N - количество каналов',
            y_name='u - Среднее время пребывания заявок в системе',
            title=f'u = f(N,B)'
        )

    @staticmethod
    def display_average_waiting_time(average_waiting_time: dict[int, float]) -> None:
        GraphicsMaker.make_plot(
            data=average_waiting_time,
            x_name='N - количество каналов',
            y_name='Среднее время ожидания',
            title=f'w = f(N,B)'
        )

    @staticmethod
    def display_queue_length(queue_length_dependency: dict[int, float]) -> None:
        GraphicsMaker.make_plot(
            data=queue_length_dependency,
            x_name='N - количество каналов',
            y_name='L - Средняя длина очереди',
            title=f'L = f(N,B)'
        )
