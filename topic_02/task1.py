import math

print("Квадратне рівняння має наступний вигляд: a*(x^2) + b*x + c = 0")
a = int(input("Уведіть a = "))
b = int(input("Уведіть b = "))
c = int(input("Уведіть c = "))

def discr(a, b, c):
    return b**2 - 4*a*c

def equation_solution(a, b, c):
    d = discr(a, b, c)
    print("Дискримінант: " + str(d))
    if d > 0:
        x1 = (-(b) + math.sqrt(d)) / (2*a)
        x2 = (-(b) - math.sqrt(d)) / (2*a)
        return f"Рівняння має два розв'язки: x1 = {x1} and x2 = {x2}"
    elif d == 0:
        x1 = (-b) / (2*a)
        return f"Рівняння має один розв'язок: x = {x1}"
    else:
        return "Рівняння не має розв'язків"

print (equation_solution(a, b, c))

    #  Два розвязки: a = 7, b = -6, c = -1, d = 64, x1 = 1, x2 = -0.142857
    #  Один розвязок: a = 25, b = -10, c = 1, d = 0, x = 0.2
    #  Немає розвязків: a = 1, b = 1, c = 9, d = -35