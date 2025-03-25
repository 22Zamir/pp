import random


class Warriors:

    def __init__(self, name, health=100):
        self.name = name
        self.health = health


warrior_1 = Warriors('Протвник-1')
warrior_2 = Warriors('проивник-2')

while warrior_1.health > 0 and warrior_2.health > 0:
    damage = random.randint(1, 2)
    if damage == 1:
        print(f'{warrior_1.name} - наносит удар!')
        warrior_2.health -= 20
        print(f'Здоровье <<{warrior_2.name}>>:{warrior_2.health}\n')
        if warrior_2.health == 0:
            print(f'{warrior_1.name} одержал победу!')
    if damage == 2:
        print(f'{warrior_2.name} - наносит удар!')
        warrior_1.health -= 20
        print(f'Здоровье <<{warrior_1.name}>>: {warrior_1.health}\n')
        if warrior_1.health == 0:
            print(f'{warrior_2.name} одержал победу!')
