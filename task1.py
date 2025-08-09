import logging
from abc import ABC, abstractmethod
from typing import Union

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} {self.spec}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self) -> None:
        logging.info(f"{self.make} {self.model} {self.spec}: Мотор заведено")


class VehicleFactory(ABC):
    @property
    @abstractmethod
    def spec(self) -> str:
        pass

    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass


class USVehicleFactory(VehicleFactory):
    @property
    def spec(self) -> str:
        return "(US Spec)"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, self.spec)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, self.spec)


class EUVehicleFactory(VehicleFactory):
    @property
    def spec(self) -> str:
        return "(EU Spec)"

    def create_car(self, make: str, model: str) -> Car:
        return Car(make, model, self.spec)

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        return Motorcycle(make, model, self.spec)


# Використання
us_factory: VehicleFactory = USVehicleFactory()

us_car: Car = us_factory.create_car("Ford", "Mustang")
us_car.start_engine()

us_motorcycle: Motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
us_motorcycle.start_engine()


eu_factory: VehicleFactory = EUVehicleFactory()

eu_car: Car = eu_factory.create_car("Volkswagen", "Jetta")
eu_car.start_engine()

eu_motorcycle: Motorcycle = eu_factory.create_motorcycle("BMW", "M5")
eu_motorcycle.start_engine()
