from tire.tire import Tire


class Carrigan(Tire):
    def __init__(self, tire_usage):
        self.tire_usage = tire_usage

    def needs_service(self):
        return False
