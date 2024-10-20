lang1 = ["Python", "C++", "Java"] 
lang2 = ["MySQL", "PHP", "HTML"]

print("Перший список: ", lang1)
print("Другий список: ", lang2)

# Додавання елементу в кінець списку
lang2.append("CSS")
print("Другий список після додавання 1 елемента: ", lang2)

# Додавання всіх елементів одного списку до другого
lang1.extend(lang2)
print("Перший список після додавання другого: ", lang1)

# Видалення останнього елементу списку
lang1.remove("CSS")
print("Перший список після видалення останнього елемента: ", lang1)

# Вставка передостаннього елементу списку
lang1.insert(5,"CSS")
print("Перший список після вставки 5-го елемента: ", lang1)

# Сортування всіх елементів списку 
lang1.sort()
print("Перший список після сортування (по алфавіту): ", lang1)

# Реверс всіх елементів списку 
lang1.reverse()
print("Перший список в зворотньому порядку: ", lang1)

# Копія 2-го списку в 3-й список
lang3 = lang2.copy()
print("Копія другого списку в 3-й lang3=", lang3)

# Очищення 2-го списку 
lang2.clear()
print("Другий список очищений lang2=", lang2)




