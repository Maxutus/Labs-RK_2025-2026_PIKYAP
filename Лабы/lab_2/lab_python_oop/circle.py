import math
from .figure import Figure
from .color import Color

class Circle(Figure):
    name = "Круг"

    def __init__(self, radius, color_name):
        self.radius = radius
        self.color = Color(color_name)

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f"{self.name} {self.color.color_name} цвета, радиус = {self.radius}, площадь = {self.area():.2f}"
