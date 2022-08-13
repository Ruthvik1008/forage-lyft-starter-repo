from abc import ABC

from car import Car
import engine


class SternmanEngine(engine):
    def __init__(self, warning_light_on):
        self.warning_lighwarning_light_ont_is_on = warning_light_on

    def needs_service(self):
        if self.warning_light_on:
            return True
        else:
            return False
