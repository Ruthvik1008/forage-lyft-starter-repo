from abc import ABC
from car import Car
import battery
from dateutil import relativedelta


class NubbinBattery(battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        # uses relative date to find difference between dates in years
        # current_date must be > last_service
        if self.last_service_date > self.current_date:
            return False
        else:
            delta = relativedelta.relativedelta(
                self.current_date, self.last_service_date)
            return delta.years >= 4
