from Student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def addNewElement(self, student: Student):
        self.students.append(student)
        print(f"Student {student.name} is appened.")

    def deleteElement(self, name: str):
        deletePosition = -1
        for student in self.students:
            if name == student.name:
                deletePosition = self.students.index(student)
                break
        if deletePosition == -1:
            print("Element was not found")
        else:
            print("Delete position " + str(deletePosition))
            del self.students[deletePosition]
        return

    def updateElement(self, student_name: str, name1, phone1, kurs1, group1):        
        for student in self.students:
            if student.name == student_name:
                student.update(name1, phone1, kurs1, group1)
                print(f"Student data {student_name} is updated.")
                return
        print(f"Student name: {student_name} not found.")

    def printAllList(self):
        for student in self.students:
            print(student)
