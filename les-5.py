# домашнеезадание №1
f = open(r"text_1.txt", "a")
while True:
    my_text = input("Введите текст для записи в файл - ")
    f.write(my_text + '\n')
    if not my_text:
        break
f.close()

# домашнеезадание №2
with open("text_2.txt") as f:
    my_line = f.readlines()
    for index, value in enumerate(my_line):
        number_of_words = len(value.split())
        print('Строка {} содержит {} слов'.format(index + 1, number_of_words))

# домашнеезадание №3
with open("text_3.txt") as f:
    my_line = f.readlines()
    sr_sum = 0
    list_sol_min = []
    print("Заработная плата сотрудников:")
    for index, value in enumerate(my_line):
        sol = int((value.split())[1])
        sr_sum = sr_sum + sol
        print(index+1, value.replace("\n", ""))
        if sol < 20000:
            list_sol_min.append((value.split())[0])
    print("Средняя заработная плата - ", round(sr_sum/(index+1)), "рублей\nСписок сотрудников получающих меньше 20000:")
    print("\n".join(list_sol_min))

# домашнеезадание №4
file_out = open("text_4_copy.txt", 'w')
file_in = open("text_4.txt", 'r')
dict = {"1": "Один", "2": "Два", "3": "Три", "4": "Четыре"}
list_new = []
for index, value in enumerate(file_in):
    file_out.write(dict.get((value.split())[2]) + " - " + str(index + 1) + "\n")
file_in.close()
file_out.close()
