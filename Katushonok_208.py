# 1.	Создайте класс "Студент", который имеет атрибуты имя и возраст, а также методы "изменить_имя" и "изменить_возраст".
# Напишите функцию, которая создает объект класса "Студент", запрашивая у пользователя его имя и возраст,
# а затем предлагает пользователю изменить имя и возраст.


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = age

    def __str__(self):
        return f'Имя студента: {self.name}, возраст: {self.age} лет.'


def new_stud():
    name = input('Введите имя студента: ')
    age = int(input('Введите возраст студента: '))
    st = Student(name, age)
    print(st)
    flag = input('Хотите ли изменить имя и возраст студента(Да/Нет)?')
    if flag == 'Да':
        st.change_name(input('Введите новое имя студента: '))
        st.change_age(int(input('Введите новый возраст студента: ')))
        print(st)

new_stud()

#2.	Напишите функцию, которая принимает на вход список чисел и возвращает сумму квадратов всех четных чисел в списке.

def squar_num(l):
    sum_list = 0
    for i in l:
        if i % 2 == 0:
            sum_list += i ** 2

    return sum_list

print(squar_num([1, 2, 4, 7, 10, 11]))


#3.	Создайте класс "Калькулятор", который имеет атрибуты "значение" и методы "сложить", "вычесть", "умножить" и "разделить".
# Напишите функцию, которая создает объект класса "Калькулятор" и позволяет пользователю выполнить несколько арифметических
# операций с его помощью.


class Calculator:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def add(self):
        return self.num_1 + self.num_2

    def sub(self):
        return self.num_1 - self.num_2

    def mul(self):
        return self.num_1 * self.num_2

    def div(self):
        return self.num_1 / self.num_2


def oper_cal():
    num_1 = float(input('Введите первое число: '))
    num_2 = float(input('Введите второе число: '))
    cl = Calculator(num_1, num_2)
    while True:
        oper = input('Введите оперцию для калькулятора(+,-,*,/): ')
        if oper == '+':
            print(cl.add())

        elif oper == '-':
            print(cl.sub())

        elif oper == '*':
            print(cl.mul())

        elif oper == '/':
            if num_2 != 0:
                print(cl.div())
            else:
                print('На ноль делить нельзя!')

        else:
            break

oper_cal()


#4.	Создайте класс "Автомобиль", который имеет атрибуты "марка", "модель", "год_выпуска", "цвет" и метод "описание",
# который выводит описание автомобиля в виде строки. Напишите функцию, которая создает объект класса "Автомобиль",
# запрашивая у пользователя информацию о марке, модели, годе выпуска и цвете, а затем выводит описание автомобиля.

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f'Марка машины {self.make}, модель {self.model}, год выпуска {self.year}, цвет машины {self.color}.'


def new_car():
    car1 = Car(input('Марка машины: '), input('Модель: '), int(input('Год выпуска: ')), input('Цвет машины: '))
    print(car1)

new_car()


#5.	Создайте класс "Сотрудник", который имеет атрибуты "имя", "фамилия", "должность" и метод "описание",
# который выводит описание сотрудника в виде строки. Создайте класс "Отдел",
# который имеет атрибуты "название" и "список_сотрудников", а также методы "добавить_сотрудника" и "удалить_сотрудника".
# Напишите функцию, которая создает объект класса "Отдел", запрашивая у пользователя его название,
# а затем предлагает пользователю добавить несколько сотрудников в отдел, после чего выводит список всех сотрудников в отделе
# и их описания. Затем функция предлагает пользователю удалить одного из сотрудников и выводит обновленный список сотрудников и их описания.


class Employee:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


    def __str__(self):
        return f'Имя Фамилия сотрудника: {self.name} {self.surname}, должность {self.position}.'

class Dept:
    def __init__(self, name_dept):
        self.name_dept = name_dept
        self.list_employees = []


    def add_employee(self, employee):
        self.list_employees.append(employee)

    def delete_employee(self, num_emp):
        self.list_employees.pop(num_emp - 1)


def creat_dep():
    dep1 = Dept(input('Введите название отдела: '))
    num_employees = int(input('Какое количество сотрудников хотите добавить в отдел?'))
    for i in range(num_employees):
        name = input('Введите имя сотрудника: ')
        surname = input('Введите фамилию сотрудника: ')
        position = input('Введите должность сотрудника: ')
        dep1.add_employee(Employee(name, surname, position))

    for i in dep1.list_employees:
        print(i)

    num_emp = int(input(f'Введите какого сотрудника по номеру хотите удалить (от 1 до {num_employees}): '))
    dep1.delete_employee(num_emp)

    for i in dep1.list_employees:
        print(i)

creat_dep()