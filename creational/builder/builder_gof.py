from collections import namedtuple


class Car:

    def __init__(self):
        self.engine = ""
        self.gearbox = ""
        self.airbags_count = 0
        self.air_condition = ""
        self.wheels = []

    def __str__(self):
        return "Car(engine={}, gearbox={}, airbags_count={}, aircondition={}, wheels={})" \
            .format(self.engine, self.gearbox, self.airbags_count, self.air_condition if self.air_condition else "None", self.wheels)


class EconomyCarBuilder:

    def __init__(self):
        self.car = Car()

    def build_engine(self):
        self.car.engine = "petrol 1.1"

    def build_gearbox(self):
        self.car.gearbox = "manual 5"

    def build_airbags(self):
        self.car.airbags_count = 1

    def build_air_condition(self):
        pass

    def build_wheel(self):
        self.car.wheels.append("steel rims 14''")

    def get_car(self):
        return self.car


class PremiumCarBuilder:

    def __init__(self):
        self.car = Car()

    def build_engine(self):
        self.car.engine = "diesel 3.2"

    def build_gearbox(self):
        self.car.gearbox = "automatic 6"

    def build_airbags(self):
        self.car.airbags_count = 10

    def build_air_condition(self):
        self.car.air_condition = "automatic with 3 zones"

    def build_wheel(self):
        self.car.wheels.append("alu rims 18''")

    def get_car(self):
        return self.car


class Director:

    def __init__(self, builder):
        self.builder = builder

    def set_builder(self, new_builder):
        self.builder = new_builder

    def construct(self):
        builder.build_engine()
        builder.build_gearbox()
        builder.build_airbags()
        builder.build_air_condition()

        for i in range(4):
            builder.build_wheel()


if __name__ == '__main__':

    builder = EconomyCarBuilder()
    director = Director(builder)

    director.construct()
    car = builder.get_car()
    print("car constructed with EconomyCarBuilder: {}".format(car))

    print("-" * 40)

    builder = PremiumCarBuilder()
    director.set_builder(builder)
    director.construct()
    car = builder.get_car()

    print("car constructed with PremiumCarBuilder: {}".format(car))
