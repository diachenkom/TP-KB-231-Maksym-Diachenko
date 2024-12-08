import csv

global students
students = []

def loadDataFromCsv(file_name):
    try:
        with open(file_name, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:        
                students.append({"name":row["name"],"phone":row["phone"],"kurs":row["kurs"],"group":row["group"]})
            print(f"Data loaded from file {file_name}.")
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    return

def saveDataToCsv(file_name):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ["name", "phone", "kurs", "group"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
        print(f"Date saved to file {file_name}.")

def printAllList():
    for elem in students:
        strForPrint = f"Student name: {elem['name']}, Phone: {elem['phone']}, Kurs: {elem['kurs']}, Group: {elem['group']}"
        print(strForPrint)

def addNewElement(name, phone, kurs, group):
    newItem = {"name": name, "phone": phone, "kurs": kurs, "group": group}
    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New element has been added")
    return

def updateElement(new_name, name, phone, kurs, group):
    for item in students:
        if item["name"] == new_name:
            print("Data to be updated:", item)
            item["name"] = name
            item["phone"] = phone
            item["kurs"] = kurs
            item["group"] = group
            print("Data after update:",item)
            return
    print("Element was not found.")

def deleteElement(name):
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Deleted position is " + str(deletePosition))
        del students[deletePosition]
    return