import math

print("Quadratic equation has the form: a*(x^2) + b*x + c = 0")
a = int(input("Enter a = "))
b = int(input("Enter b = "))
c = int(input("Enter c = "))
discr = b**2 - 4*a*c

if discr > 0:
    x1 = ((-b + math.sqrt(discr)) / 2*a)
    x2 = ((-b - math.sqrt(discr)) / 2*a)
    print("Equation has two solutions:")
    print("x1 = " + str(x1) + " and x2 = " + str(x2))
elif discr == 0:
    x1 = -(b / 2*a)
    print("Equation has one solutions, x is:" + x1)
else:
    print("Equation has not solutions")