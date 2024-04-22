# src/main/models/graph.py
import matplotlib.pyplot as plt


class GraphicsMaker:
    @staticmethod
    def make_plot(data: dict, x_name: str = 'x', y_name: str = 'y', title: str = 'Graphic') -> None:
        x_values: list = list(data.keys())
        y_values: list = list(data.values())
        plt.plot(x_values, y_values, marker='o', linestyle='-')
        plt.xlabel(x_name)
        plt.ylabel(y_name)
        plt.title(title)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
