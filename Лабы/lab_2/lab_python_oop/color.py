class Color:
    def __init__(self, color_name):
        self.__color_name = color_name

    @property
    def color_name(self):
        return self.__color_name

    @color_name.setter
    def color_name(self, value):
        self.__color_name = value
