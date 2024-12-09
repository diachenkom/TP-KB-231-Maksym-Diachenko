from oper7 import Operations

class Functions:
    def get_numbers():
        try:
            a = float(input("Input first number: "))
            b = float(input("Input second number: "))
            return a, b
        except ValueError:
            print("Wrong input. Please repeat")
            return Functions.get_numbers()

    def choose_operation():
        print("Choose type operation:")
        print("add +")
        print("subtract -")
        print("multiply *")
        print("divide /")
        choice = input("Choose (+, -, *, /) to leave enter 'exit': ")
        return choice
    
    def perform_operation(choice, a, b):
        if choice == '+':
            return Operations.add(a, b)
        elif choice == '-':
            return Operations.subtract(a, b)
        elif choice == '*':
            return Operations.multiply(a, b)
        elif choice == '/':
            return Operations.divide(a, b)
        else:
            print("Wrong choose.")
            return None

class Logger:
    def log(text1):
        log_file="calc_log.txt"
        with open(log_file, "a") as file:
            file.write(text1 + "\n")