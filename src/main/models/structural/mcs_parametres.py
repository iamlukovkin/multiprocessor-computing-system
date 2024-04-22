# src/main/models/structural/mcs_parametres.py
from enum import Enum


class MCSParametres(Enum):
    AVERAGE_QUEUE_LENGTH = 0
    AVERAGE_WAITING_TIME = 1
    AVERAGE_TIME_OF_REQUEST = 2
    SERVICE_TIME = 3
    CPU_LOAD = 4
    SINGLE_PROCESSOR_PERFOMANCE = 5

