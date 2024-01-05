# Task Nr.2:

# Create a class that would take at least five imperial system measurements and would transform with the help of static methods to metric system units.


class ImperialToMetric:
    @staticmethod
    def in_to_cm(inch: float) -> float:
        return inch * 2.54

    @staticmethod
    def oz_to_g(ounce: float) -> float:
        return ounce * 28.35

    @staticmethod
    def gal_to_l(gallon: float) -> float:
        return gallon * 3.97

    @staticmethod
    def lb_to_kg(pound: float) -> float:
        return pound * 0.45

    @staticmethod
    def yd_to_m(yard: float) -> float:
        return yard * 0.9144


print(ImperialToMetric.lb_to_kg(10))
