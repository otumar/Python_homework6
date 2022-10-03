# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

mylist = [2,3,5,9,3]
sum_odd = sum(mylist[item] for item in range(1, len(mylist), 2))
odd_el = str([mylist[item] for item in range(1, len(mylist), 2)]).strip('[]')
print(f'For the list {mylist} the sum of numbers in odd position {odd_el} is: {sum_odd}.')
