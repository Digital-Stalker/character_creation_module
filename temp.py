from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления',
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> str:
    """Выводит результат вычесления."""
    root = calculate_square_root(your_number)
    if your_number >= 0:
        return print('Мы вычислили квадратный корень из введённого вами',
                     'числа. Это будет:', root)


calc(25.5)

