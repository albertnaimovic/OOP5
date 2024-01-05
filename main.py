class Circle:
    PI = 3.14159

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return Circle.calculate_area(self.radius)

    @staticmethod
    def calculate_area(radius: float) -> float:
        return Circle.PI * radius**2


print(Circle.calculate_area(5))