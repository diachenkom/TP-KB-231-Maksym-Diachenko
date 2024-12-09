# Визначення класу Student
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

# Створення списку об'єктів класу Student
students = [
    Student("Tom", 20),
    Student("Bob", 18),
    Student("Yan", 17),
    Student("Zak", 23),
]

# Сортування списку за віком за допомогою sorted і lambda
sorted_students = sorted(students, key=lambda student: student.age)

# Виведення відсортованого списку
for student in sorted_students:
    print(student)
