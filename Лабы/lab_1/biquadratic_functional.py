import sys
import math

def read_coefficient(name, args, index):
    if len(args) > index:
        token = args[index]
        try:
            return float(token)
        except ValueError:
            print(f"Ошибка! Коэффициент {name} в командной строке ('{token}') не является числом.")
            while True:
                s = input(f"Введите коэффициент {name}: ")
                try:
                    return float(s)
                except ValueError:
                    print(f"Ошибка! Коэффициент {name} должен быть числом.")
    else:
        while True:
            s = input(f"Введите коэффициент {name}: ")
            try:
                return float(s)
            except ValueError:
                print(f"Ошибка! Коэффициент {name} должен быть числом.")

def solve_quadratic(a, b, c):
    D = b*b - 4*a*c
    print(f"Дискриминант: {D}")
    if D < 0:
        return D, []
    elif D == 0:
        x = -b / (2*a)
        return D, [x]
    else:
        sqrtD = math.sqrt(D)
        x1 = (-b + sqrtD) / (2*a)
        x2 = (-b - sqrtD) / (2*a)
        return D, sorted([x1, x2])

args = sys.argv[1:]
a = read_coefficient("A", args, 0)
while a == 0:
    print("Коэффициент A не может быть равен нулю для квадратного уравнения.")
    a = read_coefficient("A", args, 0)

b = read_coefficient("B", args, 1)
c = read_coefficient("C", args, 2)

D, roots = solve_quadratic(a, b, c)
if roots:
    print("Действительные корни:", roots)
else:
    print("Действительных корней нет.")