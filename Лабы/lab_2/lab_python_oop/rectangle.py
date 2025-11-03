from .figure import Figure
from .color import Color

class Rectangle(Figure):
    name = "Прямоугольник"

    def __init__(self, width, height, color_name):
        self.width = width
        self.height = height
        self.color = Color(color_name)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"{self.name} {self.color.color_name} цвета, ширина = {self.width}, высота = {self.height}, площадь = {self.area()}"
