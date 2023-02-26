# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('enter a number: '))
my_list = []
listnew = []

for i in range(2, n):
    if n % i == 0:
        my_list.append(i)
if my_list == listnew:
    print(f'entered number is prime [1, {n}]')
else:
    my_list.insert(0, 1)
    my_list.append(n)
    print(f'Divisors of n: {my_list}')

    k = 0
    for i in range(len(my_list)):
        for j in range(2, my_list[i] // 2 + 1):
            if (my_list[i] % j == 0):
                k += 1
        if k <= 0:
            listnew.append(my_list[i])
        k = 0
    print(f'Prime divisors of n: {listnew}')
