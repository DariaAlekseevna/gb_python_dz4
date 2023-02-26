# Даны два файла, в каждом из которых находится запись многочлена.  (дано две строки с двумя многочленами)
# Задача - сформировать файл, содержащий сумму многочленов.


# решила задачу для часного случая (уравнения в файлах equation1.txt и equation2.txt. 
# Также должна будет работать, если уравнения в одинаковой степени и все коэффициенты не нулевые
def read_file(name):
    f = open(name, 'r')
    for line in f:
        name = line
    print(name)
    f.close()
    return name

def rep_text(text):
    text = text.replace(' = 0', '')
    text = text.replace('*x^', ',')
    text = text.replace('*x', ',1')
    text = text.replace('x^', '1,')
    text = text.replace('- ', '-') 
    text = text.replace('+ ', '')         
    return text

def sep_text(text):
    list_text = text.split(' ')
    if '' in list_text:
        list_text.remove('')
    for i in range(len(list_text)):
        if len(list_text[i]) < 3:
            list_text[i] += ',0'
    return list_text

def cre_matr(list_text):
    matr = []
    for i in range(len(list_text)):
        matr.append(list(map(int, list_text[i].split(','))))
    return(matr)

def sum_matr(matr1, matr2):
    sum_matr = []
    flag = 1
    for i in range(len(matr1)):
        for j in range(len(matr2)):
            if (matr1[i][1] == matr2[j][1]):
                sum_matr.append(str(matr1[i][0] + matr2[j][0]) + '*x^' + str(matr1[i][1]))
    if  len(matr1) > len(matr2):  #в моем примере последний коэф-т во втором уравнении отсутствует, поэтому длина разная, и я его отделтно прибавляю к сумме
        sum_matr.append(str(matr1[len(matr1)-1][0]))

    # если в результате сложения коэф-т получился нулевым, то убираю его
    sum_matr1 = sum_matr.copy()
    for i in range(len(sum_matr)):
        if sum_matr[i][0] == '0':
            sum_matr1.remove(sum_matr[i])

    for i in range(len(sum_matr1)):
        if '*x^0' or '*x^1' in sum_matr1[i]:
            sum_matr1[i] = sum_matr1[i].replace('*x^0', '')
            sum_matr1[i] = sum_matr1[i].replace('^1', '')            
    return(sum_matr1)

def opposit_rep(text):
    text = text.replace('[', '')
    text = text.replace("'", '')
    text = text.replace(',', '')
    text = text.replace(' -', '-')
    text = text.replace(' ', '+')
    text = text.replace('+', ' + ')
    text = text.replace('-', ' - ')
    text = text.replace(']', ' = 0')
    return text

def write_file(t):
    f = open('equations_sum.txt', 'w')
    f.write(t)
    print(f'сумма многочленов равна многочлену: {t}')

file1 = 'equation1.txt'
file1 = read_file(file1)
file1 = rep_text(file1)
list_file1 = sep_text(file1)
matr1 = cre_matr(list_file1)

print(f'из первого уравнения отобрала коэффициенты и степерь при х: {list_file1}')
print(f'из коэфф-в и степений первого уравнения сформирован двухуровневый список: {matr1}')

file2 = 'equation2.txt'
file2 = read_file(file2)
file2 = rep_text(file2)
list_file2 = sep_text(file2)
matr2 = cre_matr(list_file2)

print(f'из второго уравнения отобрала коэффициенты и степерь при х: {list_file2}')
print(f'из коэфф-в и степений второго уравнения сформирован двухуровневый список: {matr2}')

print(f'сложила соответствующие коэфф-ты между собой и получила список слогаемых уравнения: {sum_matr(matr1, matr2)}')
sum_m = opposit_rep(str(sum_matr(matr1, matr2)))

write_file(sum_m)