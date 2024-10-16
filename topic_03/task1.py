def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Помилка: ділення на нуль не можливе"
    return x / y

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
        try:
            num1 = float(num1)
        except ValueError:
            print("Некоректне число. Спробуйте ще раз.")
            continue

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
        try:
            num2 = float(num2)
        except ValueError:
            print("Некоректне число. Спробуйте ще раз.")
            continue

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