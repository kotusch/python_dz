#ДЗ на вторник:
# В задаче про класс Human дописать 2 класса: класс House для создания дома, класс Buy_House для его покупки.
# Для того, чтобы в классе Human свойство __house сделать True, нужно использовать наследование классов. Но каких? :)




class Buy_House:

    def buy_house(self):
        self.__house = True


# Создайте класс Human.
class Human(Buy_House):
# Определите для него два статических поля: default_name и default_age.
    default_name = 'USER'
    default_age = None
# Создайте метод __init__(), который помимо self принимает еще два параметра: name и age. Для этих параметров задайте значения по умолчанию, используя свойства default_name и default_age. В методе __init__() определите четыре свойства: Публичные - name и age. Приватные - money и house.
    def __init__(self, name = default_name, age = default_age):
        # super().__init__()
        #Динамические поля
        #Публичные
        self.name = name
        self.age = age
        #Приватные
        self.__house = False
        self.__money = 1000

# Реализуйте справочный метод info(), который будет выводить поля name, age, house и money.
    def info(self):
        print(f'Имя: {self.name}, возраст: {self.age}, наличие дома: {self.__house}, денег: {self.__money}')

    def buy_house(self):
        self.__house = True
        self.__money -= 100

# Реализуйте справочный статический метод default_info(), который будет выводить статические поля default_name и default_age.
    @staticmethod
    def default_info():
        print(f'Имя по умолчанию: {Human.default_name}, возраст по умолчанию: {Human.default_age}')

# Реализуйте метод earn_money(), увеличивающий значение свойства money.
    def earn_money(self, amount):
        self.__money += amount
        print(f'Получили {amount} рублей. Текущий счет: {self.__money} рублей')




class House:
    def __init__(self, area, number_floors, price):
        self.area = area
        self.number_floors = number_floors
        self.price = price

    def house_info(self):
        print(f'Площадь дома: {self.area} кв.м, этажность дома: {self.number_floors} этажей, цена: {self.price} тыс.')




p1 = Human("Evgeniy", 29)
p1.buy_house()
p1.info()

h1 = House(100, 2, 100)
h1.house_info()