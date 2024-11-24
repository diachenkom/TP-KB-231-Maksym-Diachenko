import csv
import sys

# Початковий список студентів
students_list = [
    {"name": "Bob", "phone": "0631234567", "kurs": "2", "group": "kb-231"},
    {"name": "Emma", "phone": "0631234567", "kurs": "3", "group": "kb-222"},
    {"name": "Jon", "phone": "0631234567", "kurs": "2", "group": "kb-232"},
    {"name": "Zak", "phone": "0631234567", "kurs": "3", "group": "kb-221"}
]

def load_data_from_csv(file_name):
    global students_list
    try:
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students_list = list(reader)
            print(f"Дані завантажені з файлу {file_name}.")
    except FileNotFoundError:
        print(f"Файл {file_name} не знайдено.")

def save_data_to_csv(file_name):
    global students_list
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["name", "phone", "kurs", "group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students_list)
        print(f"Дані збережені у файл {file_name}.")

def print_all_list():
    for elem in students_list:
        str_for_print = f"Імя студента: {elem['name']}, Телефон: {elem['phone']}, Курс: {elem['kurs']}, Група: {elem['group']}"
        print(str_for_print)

def add_new_element(new_item):
#    name = input("Уведіть ім'я студента: ")
#    phone = input("Уведіть номер телефону студента: ")
#    kurs = input("Уведіть курс: ")
#    group = input("Уведіть групу: ")
#    new_item = {"name": name, "phone": phone, "kurs": kurs, "group": group}
    students_list.append(new_item)
    print("Нового студента додано")

def delete_element(name):
#   name = input("Уведіть ім'я студента якого бажаєте видалити: ")

    deletePosition = -1
    for item in students_list:
        if name == item["name"]:
            deletePosition = students_list.index(item)
        if deletePosition != -1:
            print("Видалення запису № " + str(deletePosition))
            del students_list[deletePosition]
            return

def update_element(name, item_upd):
#    name = input("Уведіть ім'я студента дані якого бажаєте редагувати: ")
    for item in students_list:
        if item["name"] == name:
            print("Дані ДО оновлення:", item)
#            item["name"] = input("Уведіть нове ім'я: ")
            item["name"] = item_upd["name"]
#            item["phone"] = input("Уведіть новий телефон: ")
            item["phone"] = item_upd["phone"]
#            item["kurs"] = input("Уведіть новий курс: ")
            item["kurs"] = item_upd["kurs"]
#            item["group"] = input("Уведіть нову групу: ")
            item["group"] = item_upd["group"]
            print("Дані ПІСЛЯ оновлення:", item)
            return
    print("Елемент не знайдено.")

def main():
    if len(sys.argv) > 1:
        load_data_from_csv(sys.argv[1])

    while True:
        choice = input("Введіть потрібну операцію [C -створити , U -Оновити, D -Видалити, P Друкувати, X Вихід]: ").lower()
        if choice == "c":
            add_new_element()
        elif choice == "u":
            update_element()
        elif choice == "d":
            delete_element()
        elif choice == "p":
            print_all_list()
        elif choice == "x":
            save_data_to_csv("lab2.csv")
            print("Вихід та збереження даних в lab2.csv.")
            break
        else:
            print("Невірний код операції, спробуйте ще раз")

if __name__ == "__main__":
    main()