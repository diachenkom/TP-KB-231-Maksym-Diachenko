from operations import get_numbers, choose_operation, perform_operation

def main():
    print("Ласкаво просимо до калькулятора!")
    while True:
        a, b = get_numbers()
        choice = choose_operation()
        if choice.lower() == 'exit':
            break
        try:
            result = perform_operation(choice, a, b)
            if result is not None:
                print("Результат:", result)
        except ValueError as e:
            print(e)
        
        continue
    
if __name__ == "__main__":
    main()