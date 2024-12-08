import StudentList
from Student import Student
import FileUtils

def main():
    student_list = StudentList.StudentList()
    file_name = "lab2.csv"

    FileUtils.FileUtils.loadDataFromCsv(file_name, student_list)
    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                name = input("Name Student: ")
                phone = input("Phone: ")
                kurs = input("Course: ")
                group = input("Group: ")
                student = Student(name, phone, kurs, group)
                student_list.addNewElement(student)
                student_list.printAllList()

            case "U" | "u":
                print("Existing element will be updated")
                name_upd = input("Enter student Name, what need update: ")
                print("Enter new data (leave the field empty, if don't want change):")
                new_name = input("New Name: ")
                phone = input("New Phone: ")
                kurs = input("New Course: ")
                group = input("New Group: ")
                student_list.updateElement(student_name=name_upd, name1=new_name, phone1=phone, kurs1=kurs, group1=group)

            case "D" | "d":
                name = input("Please enter name to be deleted: ")
                student_list.deleteElement(name)

            case "P" | "p":
                print("List will be printed")
                student_list.printAllList()

            case "X" | "x":
                FileUtils.FileUtils.saveDataToCsv("lab2.csv",student_list)
                print("Exit")
                break

            case _:
                print("Wrong chouse")

if __name__ == "__main__":
    main()
