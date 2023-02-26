# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



# в задаче диапазон коэффициентов стоит от 0 до 100, 
# но на четвертом семинаре говорили и про отрицательные коэффициенты, поэтому я сделалаот -100 до 100
# сама не додумалась делать как-то по другому, сделала через циклы, но выглядит как-то громоздско.

from random import randint, random

def write_file(t):
    f = open('equation.txt', 'w')
    f.write(t)
    print(t)

k = int(input('enter the degree of polynomial (k): '))
coeff_list = []

for i in range(k + 1):
    coeff_list.append(randint(-100,100))
print(f'коэффициенты многочлена: {coeff_list}')

j = 0
for i in range(k):
    if coeff_list[i] == 0 and j < k:
        if i == k-1:
            print('все коэффициенты при х нулевые')
        j += 1
equat = ''
if k == 0 or j == k:
    print('многочлена нет')
else:
    for i in range(k + 1):
        if coeff_list[i] == 0:    
                equat += str('')
        elif coeff_list[i] == 1:
                if i == (k - 1) == 0:
                    equat += 'x'
                elif i == 0:
                    equat += 'x^' + str(k)
                elif i == k:
                    equat += ' + 1'
                elif i == (k - 1):
                    equat += ' + x'
                else:
                    equat += ' + x^' + str(k - i)
        elif coeff_list[i] == -1:
                if i == (k - 1):
                    equat += ' -x'
                elif i == 0:
                    equat += '-x^' + str(k)
                elif i == k:
                    equat += ' -1'
                else:
                    equat += ' -x^' + str(k - i)
        else:
            if coeff_list[i] > 1:
                if i == (k - 1) == 0:
                    equat += str(coeff_list[i]) + '*x'
                elif i == (k - 1):
                    equat += ' + '+ str(coeff_list[i]) + '*x'
                elif i == 0:
                    equat += str(coeff_list[i]) + '*x^' + str(k)
                elif i == k:
                    equat += ' + ' + str(coeff_list[i])
                else:
                    equat += ' + ' + str(coeff_list[i]) + '*x^' + str(k - i)
            else:
                if i == k - 1:
                    equat += ' ' + str(coeff_list[i]) + '*x'
                elif i == k: 
                    equat += ' ' + str(coeff_list[i])
                else:
                    equat += ' ' + str(coeff_list[i]) + '*x^' + str(k - i)
    equat += ' = 0'
print(equat)

# for i in range(len(equat)):
#     print(i, equat[i])


if equat[1] == '+':
    equat = equat[2:]
if '-' in equat:
        equat = equat.replace('-', '- ')

write_file(equat)