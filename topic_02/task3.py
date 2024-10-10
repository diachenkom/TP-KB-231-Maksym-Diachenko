# Додавання
def add(a, b):
    return a + b

# Віднімання
def subtract(a, b):
    return a - b

# Множення
def multiply(a, b):
    return a * b

# Ділення
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка: Ділити на нуль не можна!"

# X в степені Y
def step(a,b):
    return a**b

def square(a):
    return a**2

# Основна функція калькулятора
def calculator():
    print("Виберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. X в степені Y")
    print("6. Обернення числа 1/Х")
    print("7. Квадратний корінь з Х")
    print("8. Квадрат числа Х")

    cod = input("Введіть код операції (1/2/3/4/5/6/7/8): ")
    if (int(cod)<1 or int(cod)>8):
        print("Неправильний ввiд Kоду операції")
        return
    elif (int(cod)>=1 and int(cod)<=5):
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
    elif (int(cod)>=6 and int(cod)<=8):
        num1 = float(input("Введіть 1 число: "))

    # Виконання арифметичної операції
    match cod:
        case '1':
            print(f"Результат: {add(num1, num2)}")
        case '2':
            print(f"Результат: {subtract(num1, num2)}")
        case '3':
            print(f"Результат: {multiply(num1, num2)}")
        case '4':
            print(f"Результат: {divide(num1, num2)}")
        case '5':
            print(f"Результат: {step(num1, num2)}")
        case '6':
            print(f"Результат: {1/num1}")
        case '7':
            print(f"Результат: {num1**0.5}")
        case '8':
            print(f"Результат: {square(num1)}")
        case _:
            print("Неправильний код операції.")

calculator()
