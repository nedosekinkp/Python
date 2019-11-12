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