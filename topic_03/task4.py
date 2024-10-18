list1 = [1, 3, 5, 7, 9]
print("Заданий список")
print(list1)

num = int(input("Введіть ціле число: ")) 

def find_position():
    for i in range(0, len(list1)-1):
        if num < list1[i]:
            list1.insert(0, num)
            print("Вставлено елемент з індексом: 0")
            break
        if num == list1[i]:
            list1.insert(i, num)
            print("Вставлено елемент з індексом: ",i)
            break
        if (list1[i] < num) and (num < list1[i+1]):
            list1.insert(i+1, num)
            print("Вставлено елемент з індексом: ",i+1)
            break                  
    else:
        list1.append(num)
        print("Додано до списку елемент з індексом: ",len(list1)-1)

    print("Cписок після вставки елемента:")
    print(list1)

find_position()