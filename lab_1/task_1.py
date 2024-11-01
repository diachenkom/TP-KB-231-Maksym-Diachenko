
## List [Item1, Item2, Item3]
## Item {"name":"Jon", "phone":"0631234567"}

# already sorted list
list = [
    {"name":"Bob", "phone":"0631234567", "kurs":"2", "group":"kb-231"},
    {"name":"Emma", "phone":"0631234567", "kurs":"3", "group":"kb-222"},
    {"name":"Jon", "phone":"0631234567", "kurs":"2", "group":"kb-232"},
    {"name":"Zak", "phone":"0631234567", "kurs":"3", "group":"kb-221"}
]

def printAllList():
    for elem in list:
        strForPrint="Student name is "+elem["name"]+", Phone is "+elem["phone"]+", Kurs № "+elem["kurs"]+", Group is "+elem["group"]
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    kurs = input("Please enter student kurs: ")
    group = input("Please enter student group: ")
    newItem = {"name": name, "phone": phone, "kurs": kurs, "group": group}
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    updatePosition = -1
    for item in list:
        if name == item["name"]:
            updatePosition = list.index(item)
            print("Current Student is: ", list[updatePosition])
            break
    if updatePosition == -1:
        print("Element was not found")
        return
    else:
        new_name = input("Enter new name: ")
        new_phone = input("Enter new phone: ")
        new_kurs = input("Enter new kurs: ")
        new_group = input("Enter new group: ")
        newItem = {"name": new_name, "phone": new_phone, "kurs": new_kurs, "group": new_group}
        
    del list[updatePosition]
    insertPosition = 0
    for item in list:
        if new_name > item["name"]:
            insertPosition += 1
        else:
            break

    list.insert(insertPosition, newItem)
    print("Element has been updated")
    return

def main():
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")
main()