#ДЗ на пятницу:
# №1. Если в функцию передаётся кортеж, то посчитать длину всех его строк.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.
# Использовать готовые типы данных, с клавиатуры ничего не вводится
# Например function([1,2,3,'a','bc8?']) -> 4 числа, 3 буквы
# function((1,2,3,'a','bc8?',7,8,9)) -> 5 символов
# function(788) -> 1
# function('788') -> 0 букв
# №2. Привяжите к предыдущей функции декоратор, который будет выводить информацию о том,
# какой тип данных вы отправили: кортеж, список, число, строку или какой-то другой тип данных

def decor_func(func):
    def wrapper(data):
        type_data = type(data)
        print('Тип данных в переданные в функию', type_data)
        return func(data)

    return wrapper


@decor_func
def func_type(data):
    if type(data) == list:
        count_num = 0
        count_let = 0
        for i in data:
            if type(i) == int:
                count_num += 1
            elif type(i) == str:
                for j in i:
                    if j.isdigit():
                        count_num += 1
                    elif j.isalpha():
                        count_let += 1

        return f'Количество букв в списке: {count_let}, количесвто чисел: {count_num}'

    elif type(data) == int:
        count_nech = 0
        my_num = str(data)
        for i in my_num:
            if int(i) % 2 != 0:
                count_nech += 1
        return f'Количество нечётных цифр: {count_nech}'

    elif type(data) == str:
        count_let = 0
        for i in data:
            if i.isalpha():
                count_let += 1
        return f'Количество букв: {count_let}'

    elif type(data) == tuple:
        count_len = 0
        for i in data:
            if type(i) == str:
                count_len += len(i)
        return f'Длина всех строк в кортеже: {count_len}'

    else:
        return f'Неправильный тип данных'


func_type([1, 2, 3, 'a', 'bc8?'])
print(func_type(788))
print(func_type('788'))
print(func_type((1, 2, 3, 'a', 'bc8?', 7, 8, 9)))
print(func_type({1:2}))