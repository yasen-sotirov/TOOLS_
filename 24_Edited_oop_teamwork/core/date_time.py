from core.engine_start import Engine

class DateTime:

    PROGRAM_START_TIME = 0

    def __init__(self, engine: Engine):
        self.engine = engine

    def set_program_start_time(self):
        print("Please, give time in 24 hours format")
        input_time = input().split(":")
        hour = int(input_time[0])
        minutes = int(input_time[1])
        time_in_minutes = hour * 60 + minutes
        DateTime.PROGRAM_START_TIME = time_in_minutes

    @staticmethod
    def convert_to_minutes(input_time: str):
        hour = int(input_time[0])
        minutes = int(input_time[1])
        time_in_minutes = hour * 60 + minutes
