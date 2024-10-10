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

    cod = input("Введіть код операції (1/2/3/4/5/6/7): ")
    if (int(cod)<1 or int(cod)>7):
        print("Неправильний ввiд Kоду операції")
        return
    elif (int(cod)>=1 and int(cod)<=5):
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
    elif (int(cod)>=6 and int(cod)<=7):
        num1 = float(input("Введіть 1 число: "))

    # Виконання арифметичної операції
    if cod == '1':
        print(f"Результат: {add(num1, num2)}")
    elif cod == '2':
        print(f"Результат: {subtract(num1, num2)}")
    elif cod == '3':
        print(f"Результат: {multiply(num1, num2)}")
    elif cod == '4':
        print(f"Результат: {divide(num1, num2)}")
    elif cod == '5':
        print(f"Результат: {step(num1, num2)}")
    elif cod == '6':
        print(f"Результат: {1/num1}")
    elif cod == '7':
        print(f"Результат: {num1**0.5}")
    else:
        print("Неправильний код операції.")

calculator()
