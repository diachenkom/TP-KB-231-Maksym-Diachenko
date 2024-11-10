from functions import add, subtract, multiply, divide

def get_numbers():
#    Ввести два числа
    try:
        a = float(input("Введіть перше число: "))
        b = float(input("Введіть друге число: "))
        return a, b
    except ValueError:
        print("Будь ласка, введіть правильне число.")
        return get_numbers()

def choose_operation():
#    Вибрати арифметичну операцію
    print("Оберіть тип операції:")
    print("Додавання +")
    print("Віднімання -")
    print("Множення *")
    print("Ділення /")
    choice = input("Ваш вибір (+, -, *, /) для виходу - exit: ")
    return choice

def perform_operation(choice, a, b):

    if choice == '+':
        return add(a, b)
    elif choice == '-':
        return subtract(a, b)
    elif choice == '*':
        return multiply(a, b)
    elif choice == '/':
        return divide(a, b)
    else:
        print("Невірний вибір операції.")
        return None