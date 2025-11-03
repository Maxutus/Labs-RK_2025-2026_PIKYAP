from .rectangle import Rectangle

class Square(Rectangle):
    name = "Квадрат"

    def __init__(self, side, color_name):
        super().__init__(side, side, color_name)
        self.side = side

    def __repr__(self):
        return f"{self.name} {self.color.color_name} цвета, сторона = {self.side}, площадь = {self.area()}"
