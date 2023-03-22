#ДЗ на пятницу:
# Написать программу для учета животных в зоопарке
# В родительском абстрактном классе Animals создать абстрактные методы для любого животного
# От родительского класса наследовать классы для конкретных видов животных
# Также использовать полиморфизм, инкапсуляцию
# При печати объектов определенного класса выводить информацию об этом объекте.


from abc import ABC, abstractmethod


class Animals(ABC):

    @abstractmethod
    def drink(self):
        pass

    @abstractmethod
    def movement(self):
        pass

    @abstractmethod
    def eat(self):
        pass


class Birds(Animals):
    def __init__(self, genus, name, age):
        self.__genus = genus
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'Род птицы {self.__genus}, кличка {self.__name}, возраст {self.__age}'

    def drink(self):
        print('Птицы пьют воду.')

    def movement(self):
        print('Птицы передвигаются с помощью крыльев.')

    def eat(self):
        print('Птицы едят в основном зерновые культуры.')


class Mammals(Animals):
    def __init__(self, genus, name, age):
        self.__genus = genus
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'Род млекопитающего {self.__genus}, кличка {self.__name}, возраст {self.__age}'

    def drink(self):
        print('Млекопитающие пьют воду')

    def movement(self):
        print('Млекопитающие передвигаются с помощью лап')

    def eat(self):
        print('Млекопитающие бывают хищниками и травоядными')


class Fish(Animals):
    def __init__(self, genus, name, age):
        self.__genus = genus
        self.__name = name
        self.__age = age

    def __str__(self):
        return f'Род рыбы {self.__genus}, кличка {self.__name}, возраст {self.__age}'

    def drink(self):
        print('Рыбы пьют воду))')

    def movement(self):
        print('Рыбы плавают с помощью хвоста')

    def eat(self):
        print('Рыбы бывают хищниками и травоядными')


bird_1 = Birds("Ара", 'Рио', 2)
print(bird_1)
bird_1.movement()

mammal_1 = Mammals('Лев', 'Лёва', 5)
print(mammal_1)
