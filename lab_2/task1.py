import csv
import sys

students_list = []

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

def add_new_element():
    name = input("Уведіть ім'я студента: ")
    phone = input("Уведіть номер телефону студента: ")
    kurs = input("Уведіть курс: ")
    group = input("Уведіть групу: ")
    new_item = {"name": name, "phone": phone, "kurs": kurs, "group": group}
    students_list.append(new_item)
    print("Нового студента додано")

def delete_element():
    name = input("Уведіть ім'я студента якого бажаєте видалити: ")
    global students_list
    students_list = [item for item in students_list if item["name"] != name]
    print(f"Видалення запису про {name} ")

def update_element():
    name = input("Уведіть ім'я студента дані якого бажаєте редагувати: ")
    for item in students_list:
        if item["name"] == name:
            print("Дані до оновлення:", item)
            item["name"] = input("Уведіть нове ім'я: ")
            item["phone"] = input("Уведіть новий телефон: ")
            item["kurs"] = input("Уведіть новий курс: ")
            item["group"] = input("Уведіть нову групу: ")
            print("Дані ПІСЛЯ оновлення:")
            return
    print("Елемент не знайдено.")

def main():
    if len(sys.argv) > 1:
        load_data_from_csv(sys.argv[1])

    while True:
        choice = input("Введіть потрібну операцію [C створити , U Оновити, D Видалити, P Друкувати, X Вихід]: ").lower()
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