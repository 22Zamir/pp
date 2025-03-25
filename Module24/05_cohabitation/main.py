import random


##############################################################################################################
##############################################################################################################
##############Код недоработан, там немного подправлять, в целом думаю так пойдет, концепация верна############
class Human:

    def __init__(self, name, house):
        self.name = name
        self.satiety = 50
        self.house = house

    def __str__(self):
        return f'{self.name} Степень сытности {self.satiety}, {self.house}'

    def eat(self):
        self.satiety += random.randint(5, 10)
        print(f'{self.name} Поел степень сытости {self.satiety}')

    def work(self):
        self.satiety -= random.randint(5, 10)
        self.house.money += random.randint(5, 10)
        print(f'{self.name} работал, бюджет: {self.house.money}')

    def play(self):
        self.satiety -= random.randint(5, 10)
        print(f'{self.name} Играл, степень сытости: {self.satiety}')

    def shop(self):
        self.house.food += random.randint(5, 10)
        self.house.money -= random.randint(5, 10)
        print(f'{self.name} сходил в магазин - {self.house.food}\nБюджета стьало:{self.house.money}')

    def is_alive(self):
        if self.satiety > 0:
            return self.name

    def one_day(self):
        num_cube = random.randint(1, 6)
        if num_cube == 1:
            self.work()
        elif num_cube == 2:
            self.eat()
        elif self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.shop()
        elif self.house.money < 50:
            self.work()
        else:
            self.play()

class House:

    def __init__(self, food=50, money=0):
        self.food = food
        self.money = money

    def __str__(self):
        return f'еды в холодильнике-{self.food} \nи денег в тумбочке {self.money}'


house_fst = House()
person1 = Human('Саня', house_fst)
person2 = Human('Вася', house_fst)

for day in range(1, 366):
    print(f'\nПрожит {day} день:')
    if person1.is_alive():
        person1.one_day()
    else:
        print(f'{person1.name}-Откис(')

    if person2.is_alive():
        person2.one_day()
    else:
        print(f'{person2.name}-Откис(')

