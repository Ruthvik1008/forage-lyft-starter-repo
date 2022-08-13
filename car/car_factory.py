

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car.car import Car
from ..engine.capulet_engine import CapuletEngine
from ..engine.sternman_engine import SternmanEngine
from ..engine.willoughby_engine import WilloughbyEngine


#Factory Design Pattern
class CarFactory:
	def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
		engine = CapuletEngine(current_mileage, last_service_mileage)
		battery = SpindlerBattery(last_service_date, current_date)
		car = Car(last_service_date, engine, battery)
		return car

	def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
		engine = WilloughbyEngine(current_mileage, last_service_mileage)
		battery = SpindlerBattery(last_service_date, current_date)
		car = Car(last_service_date, engine, battery)
		return car

	def create_palindrome(current_date, last_service_date, warning_light_on):
		engine = SternmanEngine(last_service_date, warning_light_on)
		battery = SpindlerBattery(last_service_date, current_date)
		car = Car(last_service_date, engine, battery)
		return car

	def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
		engine = WilloughbyEngine(current_mileage, last_service_mileage)
		battery = NubbinBattery(last_service_date, current_date)
		car = Car(last_service_date, engine, battery)
		return car

	def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
		engine = CapuletEngine(current_mileage, last_service_mileage)
		battery = NubbinBattery(last_service_date, current_date)
		car = Car(last_service_date, engine, battery)
		return car