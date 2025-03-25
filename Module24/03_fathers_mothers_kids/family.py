import random


class Parent:
    """"Формируем"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.child = []

    def info(self):
        """Выводим информацию"""
        print(self.name, self.age, '\nДети:')
        for i in self.child:
            print(f'{i.name} {i.age} {i.state_calm} {i.state_hungry}')

    def hungry(self):
        """"Если голоден - накормить"""
        for child in self.child:
            if 'Голоден' in child.state_hungry:
                print(f'{child.name} - голоден, накормим')
                child.state_hungry = 'Неголоден'

    def calm(self):
        """"Если неспокоен - успокоить"""
        for child in self.child:
            if 'Неспокоен' in child.state_calm:
                print(f'{child.name} Неспокоен - успокоим')
                child.state_calm = 'Спокоен'

    def add_child(self, child):
        """"Проверям детей под условие задачи"""
        if child.age < 16:
            self.child.append(child)
            print(f'{child.name} Добавлен в список')
        else:
            print(f'Ты не ребенок - {child.name}')


class Child:
    """"Формируем детей)))"""
    state_calm = ['Неспокоен', 'Спокоен']
    state_hungry = ['Голоден', 'Неголоден']

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.state_calm = random.choice(Child.state_calm)
        self.state_hungry = random.choice(Child.state_hungry)
