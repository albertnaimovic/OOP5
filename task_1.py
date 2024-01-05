# Task Nr.1:

# Create a class which takes temperature measurements in Kelvins and add static methods to transform those to Celsius and Fahrenheit units.
from abc import ABC


class Base(ABC):
    @staticmethod
    def transform_celsius() -> float:
        pass

    @staticmethod
    def transform_fahrenheit() -> float:
        pass


class Temperature(Base):
    BASE_KELVIN_VALUE = 273.15
    BASE_FAHRENHEIT_VALUE = 32

    @staticmethod
    def transform_celsius(kelvin) -> float:
        BASE_KELVIN_VALUE = 273.15
        return kelvin - BASE_KELVIN_VALUE

    @staticmethod
    def transform_fahrenheit(kelvin) -> float:
        return round(1.8 * (kelvin - Temperature.BASE_KELVIN_VALUE) + Temperature.BASE_FAHRENHEIT_VALUE, 2)


print(Temperature.transform_fahrenheit(250))
