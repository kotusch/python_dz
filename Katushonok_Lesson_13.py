#ДЗ на вторник:
# 1. Написать рекурсивную функцию, которая определяет, является ли строка палиндромом
# (одинаково читается в обе стороны: герег, лол, мам, level и тд.)
#Шаблон:

def is_palindrome(stroka):
    if len(stroka) < 2:
        return True
    elif stroka[0] != stroka[-1]:
        return False
    else:
        return is_palindrome(stroka[1:-1])

print(is_palindrome("level"))


#2. Написать рекурсивную функцию для подсчета количества элементов в списке.

def count_elem(my_list):
  if my_list == []:
    return 0
  return 1 + count_elem(my_list[1:])

print(count_elem(['a','b', 20, 30, 40, 5]))


#3. Этот код отсортирует список строк по последнему символу в каждой строке.
    # Здесь использована лямбда-функция в качестве ключа в сортировке.
#     # Измените код так, чтобы сортировка была по второму символу каждой строки

strings = ['apple', 'banana', 'cherry', 'date']
sorted_strings = sorted(strings, key=lambda s: s[2])
# sorted_strings_1 = sorted(strings, key=lambda s: s[1])
print(sorted_strings) # Output: ['cherry', 'date', 'apple', 'banana']


#4. Напишите функцию make_adder(n),
# которая принимает целое число n и возвращает внутреннюю функцию,
# которая может прибавлять этот n к любому другому целому числу.

def make_adder(n):
    def adder(x):
        return x + n
    return adder

add_1 = make_adder(1)
add_2 = make_adder(10)

print(add_1(4))
print(add_2(8))
print(make_adder(10)(20))

#5. Напишите функцию counter(), которая возвращает внутреннюю функцию increment(),
# которая увеличивает счетчик на 1 каждый раз, когда она вызывается.

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

func_1 = counter()

print(func_1())
print(func_1())
print(func_1())