# src/main/views/mcs_view.py

class MCSView:
    @staticmethod
    def display_parametres(params: list[float]) -> str:
        result: str = ""
        result += f"Performance: {params[0]}\n"
        result += f"CPU load: {params[1]}\n"
        result += f"Average queue length: {params[2]}\n"
        result += f"Average waiting time: {params[3]}\n"
        result += f"Average time of stay: {params[4]}\n"

        return result
