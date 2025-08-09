from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self):
        print(f"{self.make} {self.model} {self.spec}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make, model, spec):
        self.make = make
        self.model = model
        self.spec = spec

    def start_engine(self):
        print(f"{self.make} {self.model} {self.spec}: Мотор заведено")


class VehicleFactory:
    @property
    @abstractmethod
    def spec(self):
        pass

    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):
    @property
    def spec(self):
        return "(US Spec)"

    def create_car(self, make, model):
        return Car(make, model, self.spec)

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, self.spec)


class EUVehicleFactory(VehicleFactory):
    @property
    def spec(self):
        return "(EU Spec)"

    def create_car(self, make, model):
        return Car(make, model, self.spec)

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, self.spec)


# Використання
us_factory = USVehicleFactory()

us_car = us_factory.create_car("Ford", "Mustang")
us_car.start_engine()

us_motorcycle = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
us_motorcycle.start_engine()


eu_factory = EUVehicleFactory()

eu_car = eu_factory.create_car("Volkswagen", "Jetta")
eu_car.start_engine()

eu_motorcycle = eu_factory.create_motorcycle("BMW", "M5")
eu_motorcycle.start_engine()
