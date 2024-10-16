list1 = [1, 3, 5, 7, 9]
print("Заданий список")
print(list1)

num = int(input("Введіть ціле число: ")) 

for i in range(0, len(list1)-1):
# Якщо число менше 0-го елементу списку
    if num < list1[i]:
        list1.insert(0, num)
        print("Вставлено елемент з індексом: 0")
        break
# Якщо число рівне одному з елементів
    if num == list1[i]:
        list1.insert(i, num)
        print("Вставлено елемент з індексом: ",i)
        break
# Якщо число в діапазоні між 2-ма сусідніми елем-ми    
    if (list1[i] < num) and (num < list1[i+1]):
        list1.insert(i+1, num)
        print("Вставлено елемент з індексом: ",i+1)
        break                  
else:
    list1.append(num)
    print("Додано до списку елемент з індексом: ",len(list1)-1)

print("Cписок після вставки елемента:")
print(list1)


