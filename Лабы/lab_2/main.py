from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from termcolor import colored

def main():
    N = 7

    rect = Rectangle(N, N, "синего")
    circle = Circle(N, "зелёного")
    square = Square(N, "красного")

    print(colored(rect, "blue"))
    print(colored(circle, "green"))
    print(colored(square, "red"))

if __name__ == "__main__":
    main()
