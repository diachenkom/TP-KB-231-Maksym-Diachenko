import csv
from StudentList import StudentList
from Student import Student

class FileUtils:
    def loadDataFromCsv(file_name: str, student_list: StudentList):
        try:
            with open(file_name, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        name=row['name'],
                        phone=row['phone'],
                        kurs=row['kurs'],
                        group=row['group']
                    )
                    student_list.addNewElement(student)
                print(f"List students is loaded from file: {file_name}.")
        except FileNotFoundError:
            print(f"File {file_name} not found.")
        except Exception as e:
            print(f"Error reading file: {e}")

    def saveDataToCsv(file_name: str, student_list: StudentList):
        try:
            with open(file_name, mode='w') as file:
                fieldnames = ["name", "phone", "kurs", "group"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for student in student_list.students:
                    writer.writerow({
                        "name": student.name,
                        "phone": student.phone,
                        "kurs": student.kurs,
                        "group": student.group
                    })
                print(f"Students list is saved to file: {file_name}.")
        except Exception as e:
            print(f"Error reading file: {e}")
