a = float(input("Введите коэффициент для x2: "))
b = float(input("Введите коэффициент для x: "))
c = float(input("Введите коэффициент постоянной: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    x1: float = (-b + (discriminant) ** 0.5) / (2 * a)
    x2 = (-b - (discriminant) ** 0.5) / (2 * a)
    print(f"Решение для {x1} и {x2}")
elif discriminant == 0:
    x = -b / (2 * a)
    print(f"Решение для {x}")
else:
    real_part: float = -b / (2 * a)
    imaginary_part = ((abs(discriminant)) ** 0.5) / (2 * a)
    print(f'Решение для {real_part} + {imaginary_part}i и {real_part} - {imaginary_part}i')