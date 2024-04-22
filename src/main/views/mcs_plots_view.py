# src/main/views/mcs_plots_view.py
from matplotlib import pyplot as plt


class PlotsView:
    @staticmethod
    def display_anything(data: dict, title: str, x_axis: str, y_axis: str) -> None:
        plt.figure()
        plt.title(title)
        for perfomance in data:
            plt.plot(data[perfomance].keys(), data[perfomance].values(), label=f'B = {perfomance/1000} оп/с')
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        plt.legend()
        plt.show()

    @staticmethod
    def display_average_waiting_time(data: dict) -> None:
        PlotsView.display_anything(data, 'w = f(N, B)', 'Количество каналов, N', 'Среднее время ожидания, w')

    @staticmethod
    def display_average_time_of_request(data: dict) -> None:
        PlotsView.display_anything(data, 'u = f(N, B)', 'Количество каналов, N', 'Среднее время обработки запроса, u')

    @staticmethod
    def display_average_queue_length(data: dict) -> None:
        PlotsView.display_anything(data, 'l = f(N, B)', 'Количество каналов, N', 'Средняя длина очереди, l')
