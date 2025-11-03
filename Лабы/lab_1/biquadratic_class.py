import sys
import math

class CoefficientReader:
    def set_args(self, args):
        self.args = args

    def read(self, name, index):
        if len(self.args) > index:
            token = self.args[index]
            try:
                return float(token)
            except ValueError:
                print(f"Ошибка! Коэффициент {name} в командной строке ('{token}') не является числом.")
                return self._read_from_input(name)
        else:
            return self._read_from_input(name)

    def _read_from_input(self, name):
        while True:
            s = input(f"Введите коэффициент {name}: ")
            try:
                return float(s)
            except ValueError:
                print(f"Ошибка! Коэффициент {name} должен быть числом.")

class QuadraticEquation:
    def set_coefficients(self, a, b, c):
        if a == 0:
            raise ValueError("Коэффициент A не может быть равен нулю для квадратного уравнения.")
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        return self.b * self.b - 4 * self.a * self.c

    def solve(self):
        D = self.discriminant()
        print(f"Дискриминант: {D}")
        if D < 0:
            return []
        elif D == 0:
            x = -self.b / (2 * self.a)
            return [x]
        else:
            sqrtD = math.sqrt(D)
            x1 = (-self.b + sqrtD) / (2 * self.a)
            x2 = (-self.b - sqrtD) / (2 * self.a)
            return sorted([x1, x2])


args = sys.argv[1:]

reader = CoefficientReader()
reader.set_args(args)

a = reader.read("A", 0)
while a == 0:
    print("Коэффициент A не может быть равен нулю для квадратного уравнения.")
    a = reader.read("A", 0)

b = reader.read("B", 1)
c = reader.read("C", 2)

equation = QuadraticEquation()
equation.set_coefficients(a, b, c)

roots = equation.solve()
if roots:
    print("Действительные корни:", roots)
else:
    print("Действительных корней нет.")