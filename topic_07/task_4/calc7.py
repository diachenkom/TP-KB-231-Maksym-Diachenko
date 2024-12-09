from func7 import Functions, Logger

print("Start calculator")
while True:
    a, b = Functions.get_numbers()
    choice = Functions.choose_operation()
    Logger.log(f"{a} {choice} {b}")
    if choice.lower() == 'exit':
        break
    try:
        result = Functions.perform_operation(choice, a, b)
        if result is not None:
            print("Result = ", result)
            str_res="Result = " + str(result) +"\n"
            Logger.log(f"{str_res}")
    except ValueError as e:
        print(e)
    continue