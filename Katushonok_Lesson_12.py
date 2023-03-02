# #ДЗ на пятницу:
# #ДЗ пушим на гитхаб и отправляем мне ссылку на сам файл
# 1. Напишите функцию, которая принимает на вход два аргумента и возвращает их сумму.

def sum_func(a, b):
    return a + b

print(sum_func(2,5))

# 2. Напишите функцию, которая принимает на вход список чисел и возвращает их среднее значение.

def av_value(*args):
    return sum(*args)/len(*args)

print(av_value([2, 4, 6, 8, 10]))

# 3. Напишите функцию, которая принимает на вход число и возвращает True, если оно четное, и False, если оно нечетное.

def check_num(num):
    return num % 2 == 0

print(check_num(10))

# 4. Напишите функцию, которая принимает на вход список и возвращает новый список, содержащий только уникальные элементы из исходного списка.

def uniq_elem(*args):
    return list(set(*args))

print(uniq_elem([2, 4, 6, 8, 10,10, 2, 4, 4, 4]))


# 5. Решите задачу с использованием вложенной функции is_square. Предположим, у нас есть список чисел и мы хотим найти все числа, которые являются квадратами других чисел в этом списке.
# Шаблон кода (ориентировачный):


def find_square_numbers(numbers):
    def is_square(number):
        return number * number in numbers

    new_numbers_list = []
    for i in numbers:
        if is_square(i):
            new_numbers_list.append(i)

    return new_numbers_list


print(find_square_numbers([2, 4, 8, 10, 11, 16,64, 100]))