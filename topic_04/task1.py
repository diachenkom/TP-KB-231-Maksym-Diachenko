def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    while True:
        try:
            a = x / y
            break
        except ZeroDivisionError:
            print("Помилка ділення на нуль.")
            y = input("Введіть НЕ нульове друге число: ")
            y = CheckValue(y)
            continue
    return a

def CheckValue(num):
    while True:
        try:
            num = float(num)
            break
        except ValueError:
            print("Некоректне число")
            num = input("Введіть коректне число: ")
    return num

def calculator():
    print("Доступні операції:")
    print("Додавання: +")
    print("Віднімання: -")
    print("Множення: *")
    print("Ділення: /")
    print("Для виходу введіть 'exit'.")

    while True:
        # Запит першого числа
        num1 = input("Введіть перше число: ")
        if num1.lower() in ['exit']:
            print("Завершення роботи калькулятора.")
            break
        else:
            num1=CheckValue(num1)
        
        # Запит операції
        operation = input("Введіть операцію (+, -, *, /): ")
        if operation.lower() in ['exit']:
            print("Завершення роботи калькулятора.")
            break
        if operation not in ['+', '-', '*', '/']:
            print("Некоректна операція. Спробуйте ще раз.")
            continue
                
        # Запит другого числа
        num2 = input("Введіть друге число: ")
        if num2.lower() in ['exit']:
            print("Завершення роботи калькулятора.")
            break
        else:
            num2=CheckValue(num2)

        # Виконання обчислення
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        print(f"Результат: {result}\n")

calculator()