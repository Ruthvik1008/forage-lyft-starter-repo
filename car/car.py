from abc import ABC, abstractmethod

from .serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, last_service_date, engine, battery):
        self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        pass
