# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 2n + 1.

f = '2*x+1'
n = int(input('Enter the number of elements in the dictionary: '))
d = {x: eval(f) for x in range(1, n+1)}
print(f'For {n = }: {d}')

