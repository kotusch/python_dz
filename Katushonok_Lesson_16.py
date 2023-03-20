class Calkulator:

    # def __init__(self, val_1=None, val_2=None, operat=None):
    #     self.num_1 = val_1
    #     self.num_2 = val_2
    #     self.oper = operat
    #
    #     if self.oper == '+':
    #         print(self.add())
    #
    #     elif self.oper == '-':
    #         print(self.minus())
    #
    #     elif self.oper == '*':
    #         print(self.umpn())
    #
    #     elif self.oper == '/':
    #         if self.num_2 != 0:
    #             print(self.delen())
    #         else:
    #             print('На ноль делить нельзя!')

    def add(self, num_1, num_2):
        return num_1 + num_2

    def minus(self, num_1, num_2):
        return num_1 - num_2

    def __umpn(self, num_1, num_2):
        return num_1 * num_2

    def _delen(self, num_1, num_2):
        return num_1 / num_2

cal1 = Calkulator()

while True:
    oper = input('Ведите операцию для калькулятора(+, - ,/, *, или N для завершения: ')
    if oper != 'N':
        num_1 = float(input('Введите первое число: '))
        num_2 = float(input('Введите второе число: '))
        if oper == '+':
            print(cal1.add(num_1, num_2))

        if oper == '-':
            print(cal1.minus(num_1, num_2))

        if oper == '*':
            print(cal1.umpn(num_1, num_2))

        if oper == '/':
            if num_2 != 0:
                print(cal1.delen(num_1, num_2))
            else:
                print('На ноль делить нельзя!')

    else: break

print(cal1.minus(10, 5))
print(cal1.add(10, 5))

print(cal1.__umpn(2,3))
print(cal1._delen(6, 3))