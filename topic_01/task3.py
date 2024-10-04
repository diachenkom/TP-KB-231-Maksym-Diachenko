def discr(a, b, c):
    return b**2 - 4*a*c

print("Quadratic equation has the form: a*(x**2) + b*x + c = 0")
a = int(input("Enter a = "))
b = int(input("Enter b = "))
c = int(input("Enter c = "))
d = discr(a, b, c)
print("Discriminant is: " + str(d))