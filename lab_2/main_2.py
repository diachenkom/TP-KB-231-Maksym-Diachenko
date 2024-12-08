from sys import argv
from Lab2 import loadDataFromCsv, saveDataToCsv, printAllList, addNewElement, updateElement, deleteElement 

print(f"Script name: {argv[0]}")
print(f"Input parameter: {argv[1]}")

file_name = argv[1]
students = []
def main():
    loadDataFromCsv(file_name)
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                name = input("Name Student: ")
                phone = input("Phone: ")
                kurs = input("Course: ")
                group = input("Group: ")
                addNewElement(name, phone, kurs, group)
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                name_upd = input("Enter student Name, what need update: ")
                print("Enter new data (leave the field empty, if don't want change):")
                new_name = input("New Name: ")
                phone = input("New Phone: ")
                kurs = input("New Course: ")
                group = input("New Group: ")
                updateElement(name_upd, new_name, phone, kurs, group)
            case "D" | "d":
                name = input("Please enter name to be delted: ")
                deleteElement(name)
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                saveDataToCsv(file_name)
                print("Exit")
                break
            case _:
                print("Wrong chouse")

if __name__ == "__main__":
    main()