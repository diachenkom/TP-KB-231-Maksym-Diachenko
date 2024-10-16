# Словник для прикладу
my_dict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(my_dict)

# Оновлення (зміна) елемента словника
my_dict.update({"year": 1980})
print(my_dict)

# Видалення елемента словника по вказаному ключу
del my_dict["year"]
print(my_dict)

# Список усіх ключів словника
my_keys = my_dict.keys()
print(my_keys)

# Список усіх значень словника
my_values = my_dict.values()
print(my_values)

# Додати новi елемент до словника
my_dict["color"] = "dark"
my_dict["year"] = 1990 
print(my_dict)

# Отримати список усіх елементів словника
my_items=my_dict.items()
print(my_items)

# Отримати усіх елементів словника
my_dict.clear()
print(my_dict)
