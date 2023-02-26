# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

entered_list = list(map(int,input('enter numbers separated by space:').split()))
print(f'Entered list: {entered_list}')

print(f'The list of unique elements: {list(set(entered_list))}')

