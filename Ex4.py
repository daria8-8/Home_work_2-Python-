from random import randint
def read_file():
    with open('file.txt', 'r') as text:
        index = [int(i) for i in text]
    return index

n = int(input("Введите число N: "))
numbers = []
for i in range(n):
     numbers.append(randint(-n,n+1))
print(numbers)
lst_index = read_file()
result = 1
for i in range(len(lst_index)):
    result *= numbers[lst_index[i]-1]
print(f"Произведение чисел на позициях {read_file()} = {result}")


# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
# в одной строке одно число.





# N = int(input('Введите число: '))
# numbers = []
# for i in range(N):
#     numbers.append(randint(-N,N+1))
    
# print(numbers)

# x = int(input('Введите позицию 1 элемента: '))
# y = int(input('Введите позицию 2 элемента: '))

# for i in range(len(numbers)):
#     result = numbers[x -1]*numbers[y - 1]
# print('Произведение элементов =', result)