num = int(input("Введите число N: "))
sum = 0
for i in range(1,num+1):
    sum += (1+1/i)**i
print(round(sum,2))

# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.