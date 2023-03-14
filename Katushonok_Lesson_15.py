# ДЗ на вторник:
# 1. Создайте класс Person, который имеет атрибуты name и age, а также метод greet() (выводит приветствие на экран с именем персоны).

class Person:
    name = 'Zhenya'
    age = 29

    def greet(self):
        print(f'Hello, {self.name}!')

p1 = Person()
p1.greet()
p2 = Person()
p2.name = 'Alina'
p2.greet()

# 2. Создайте класс Car, который имеет атрибуты make, model и year, а также метод get_info() (возвращает строку, содержащую информацию о машине).


class Car:
    make = 'Opel'
    model = 'Vectra'
    year = 2010

    def get_info(self):
        return f'Марка машины {self.make}, модель {self.model}, выпущена в {self.year} году.'

car1 = Car()
print(car1.get_info())
car2 = Car()
car2.make, car2.model, car2.year = 'Renault', 'Duster', 2018
print(car2.get_info())