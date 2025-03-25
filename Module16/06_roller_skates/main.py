N = []
K = []
count = 0

kol_vo_rolikov = int(input('Введите кол-во роликов:'))

for i in range(kol_vo_rolikov):
    N.append(int(input(f'Введите размер {i+1}-ой пары:')))


kol_vo_lyd = int(input('Кол-во людей: '))
for x in range(kol_vo_lyd):
   K.append(int(input(f'Размер ноги {x + 1}человека:')))

for num in K:
    for kol_vo in range(len(N)):
        if N[kol_vo] >= num:
            N.remove(N[kol_vo])
            count += 1
            break

print(f'Наибольшее количество людей, которые могут взять ролики:{count}')

