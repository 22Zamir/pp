class Property():

    def __init__(self, worth):
        self.worth = worth

    def tax(self):
        pass


class Apartment(Property):
    name = 'Квратира'

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 1000


class Car(Property):
    name = 'Машина'

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 200


class CountryHouse(Property):
    name = 'Дача'

    def __init__(self, worth):
        super().__init__(worth)

    def tax(self):
        return self.worth / 500


sum_nalog = 0
amount_money = int(input('Введите количество имеющихся денег: '))
wroth_1 = float(input('"Ценник квартиры: '))
wroth_2 = float(input('Ценник машины: '))
wroth_3 = float(input('Ценник дачи:: '))

tax_list = [Apartment(wroth_1), Car(wroth_2), CountryHouse(wroth_3)]

for i in tax_list:
    print(f'{i.name}-{i.tax()}')
    sum_nalog += i.worth

if sum_nalog > amount_money:
    print(f'Не хватает денег, чтобы оплатить налог. Нужно - {sum_nalog - amount_money}')
else:
    print(f'Пора платить налоги, сумма - {sum_nalog}')
