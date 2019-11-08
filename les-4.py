# домашнеезадание №1
from sys import argv
script_name, first_param, second_param, third_param = argv
print("Расчет заработной платы сотрудника: ", int(first_param) * int(second_param) + int(third_param))

# домашнеезадание №2
my_list = [0, 1, 7, 88, 89, 2, 6]
print(range(len(my_list)))
new_list = [my_list[el] for el in range(len(my_list)) if el > 0 and my_list[el-1] < my_list[el]]
print(new_list)

# домашнеезадание №3
print([el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0])

# домашнеезадание №4
my_list = [1, 33, 1, 0, 33, 33, 5, 994, 0]
my_set = set()
unique_list = [x for x in my_list if x not in my_set and (my_set.add(x) or True)]
print(unique_list)

# домашнеезадание №5
from functools import reduce

def my_func(prev_el, el):
    return prev_el * el

print(reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0]))

# домашнеезадание №6
from itertools import count, cycle

a = int(input("Введите число, начиная с которого будет созадан последовательность - "))
b = int(input("Введите количество элементов последовательности - "))
for el in count(a):
    if el > b:
        break
    else:
        print(el)

a = str(input("Введите буквы, которые будут повторяться - "))
b = int(input("Введите количество элементов последовательности - "))
с = 0
for el in cycle(a):
    if с >= b:
        break
    print(el)
    с += 1

# домашнеезадание №7
def fac(n): # применяю рекурсивнуюфункцию, которую проходили на курсе Основы программирования, yield не разобрался оказалось очень сложно?
    if n == 0:
        return 1
    return fac(n - 1) * n
d = int(input("Факториал числа - "))
print(fac(d))
