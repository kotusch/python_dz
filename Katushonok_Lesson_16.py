class Calkulator:

    def __init__(self, val_1=int(input('Введите первое число: ')), val_2=int(input('Введите второе число: ')), operat=input('Введите операцию для калькулятора: ')):
        self.num_1 = val_1
        self.num_2 = val_2
        self.oper = operat

        if self.oper == '+':
            print(self.add())

        elif self.oper == '-':
            print(self.minus())

        elif self.oper == '*':
            print(self.umpn())

        elif self.oper == '/':
            if self.num_2 != 0:
                print(self.delen())
            else:
                print('На ноль делить нельзя!')



    def add(self):
        return self.num_1 + self.num_2

    def minus(self):
        return self.num_1 - self.num_2

    def umpn(self):
        return self.num_1 * self.num_2

    def delen(self):
        return self.num_1 / self.num_2

cal1 = Calkulator()

# while True:
#     oper = input('Ведите операцию для калькулятора(+, - ,/, *, или N для завершения: )')
#     if oper != 'N':
#         Calkulator(oper)
#     else: break

