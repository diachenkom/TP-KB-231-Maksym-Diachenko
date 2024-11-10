import random

options = ["stone", "scissor", "paper"]
my_option = input("Enter your choice (stone, scissor, paper): ")

if my_option not in options:
    print("Wrong value, try again.")
else:
    pc_option = random.choice(options)
    print(f"Computer choose: {pc_option}")

    if my_option == pc_option:
        print("Nobody won!")
    elif (my_option == "stone" and pc_option == "scissor") or (my_option == "scissor" and pc_option == "paper") or (my_option == "paper" and pc_option == "stone"):
        print("You won!")
    else:
        print("Computer won!")
