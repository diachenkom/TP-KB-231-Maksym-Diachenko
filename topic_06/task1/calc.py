from operations import get_numbers, choose_operation, perform_operation

try:
    file1 = open("test.txt", "a")
    file1.write("\nЖурнал роботи калькулятора\n")
    print("Калькулятор арифметичних функцій")
    while True:
        a, b = get_numbers()
        choice = choose_operation()
        file1.write(str(a) + " " + choice + " " + str(b) + " ")
        if choice.lower() == 'exit':
            break
        try:
            result = perform_operation(choice, a, b)
            if result is not None:
                print("Результат = ", result)
                file1.write("Результат = " + str(result) +"\n")
        except ValueError as e:
            print(e)
        continue
finally:
    file1.close()