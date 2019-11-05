#Первое задание

def delim_dva (var_1, var_2):
    try:
        print (var_1/var_2)
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    else:
        return(var_1/var_2)


try:
    var_1 = float(input("Укажите первое число: "))
    var_2 = float(input("Укажите второе число: "))
except ValueError:
    print("Вы ввели не число! Введите число")
else:
    delim_dva(var_1, var_2)

#Второе задание - постарался максимально сократить код

def passport(name, surname, age, city, email, telephon):
    print ("Имя "+ name + ", фамилия " + surname + ", год рождения " + age + ", город проживания " + city + ", e-mail: " + email + ", телефон: " + telephon)

passport(age=input("Введите ваш год рождения: "), name=input("Введите ваше имя: "), email=input("Введите ваш email: "), surname=input("Введите вашу фамилию: "), telephon=input("Введите ваш номер телефона: "), city=input("Введите ваш город проживания: "))


#Третье задание - решил не выяснять какие два числа больше а выяснить сразу какой будет максимальный ответ, цикл делать не стал - всего три значения

def my_func(var_1, var_2, var_3):
    max_number = (var_2 + var_3)
    if (max_number <= var_1 + var_2):
        max_number = var_1 + var_2
    if (max_number <= var_1 + var_3):
        max_number = var_1 + var_3
    return(max_number)
print(my_func(8, 1, 7))

#Четвертое задание

def my_func(x, y):
    itog = 1
    i = 1
    for i in range(abs((y))):
        itog = itog * 1 / x
    return itog

print(my_func(2, -5))

