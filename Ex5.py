from random import randint
def list_1(initial_list):
    list = initial_list[:]
    list_length = len(list)
    for i in range(list_length):
        index_random = randint(0, list_length - 1)
        temp = list[i]
        list[i] = list[index_random]
        list[index_random] = temp
    return list
num = int(input("Введите количество элементов списка: "))
list = []
for i in range(num): 
    list.append(randint(0, 100))
list_2 = list_1(list)
print(f"Исходный список: {list}")
print(f"Перемешанный список: {list_2}")

# Реализуйте алгоритм перемешивания списка.
