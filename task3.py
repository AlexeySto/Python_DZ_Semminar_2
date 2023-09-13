# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("Введите число N: "))

res = 1
count = 1
while res < n:
    print(res, end=" ")
    res = 2 ** count
    count += 1
