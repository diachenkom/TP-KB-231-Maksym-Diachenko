student_grades = [
    ('Zak', 10),
    ('Ann', 12),
    ('Steve', 8),
    ('Maksym', 11),
]
print("Несортований список студентів:")
print(student_grades)

a = sorted(student_grades, key=lambda elem: elem[1])   
print("Сортування за оцінками:")
print(a)

b = sorted(student_grades, key=lambda elem: elem[0])
print("Сортування за іменем:")
print(b)