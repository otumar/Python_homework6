# Задание 2_1. Дана последовательность чисел.
# Получить список уникальных элементов заданной последовательности.

mylist = [1,3,4,6,7,8,5,4,3,1]
resultlist = list(filter(lambda a: mylist.count(a) == 1, mylist))
print(f'For the list {mylist} the list of unique elements is {resultlist}')
