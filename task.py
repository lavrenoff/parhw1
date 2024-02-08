# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_list_imperative(numbers):    
    n=len(numbers)
    for i in range(n):
        for j in range(0,n-i-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1]=numbers[j+1], numbers[j]

numbers=[10,89,96,36,95,47,1,2,36]                

print('Сортировка по убыванию в императивном стиле:',sort_list_imperative(numbers))
