N = []
kol_people = int(input('Кол-во человек: '))
K = int(input('Какое число в считалке?'))
print(f'Значит, выбывает каждый {K} человек')
start = 0


for i in range(kol_people):
    N.append(i + 1)

while len(N) > 1:
    print(f'Текущий круг людей: {N}')
    delete = start % len(N)
    print(f'Начало счёта с номера:{N[delete]}')
    start = (delete + K - 1) % len(N)
    print(f'Выбывает человек под номер: {N[start]}')
    N.remove(N[start])
    print()
    print(f'Остался человек под номер {N[0]}')





