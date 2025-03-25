kol_zakazov = int(input('Введите кол-во заказов: '))
user_dict = {}
for number in range(1, kol_zakazov + 1):
    order = input(f'{number}-ый заказ: ').split()
    if order[0] in user_dict:
        if order[1] in user_dict[order[0]]:
            user_dict[order[0]][order[1]] += int(order[2])
        else:
            user_dict[order[0]][order[1]] = order[2]
    else:
        user_dict[order[0]] = dict({order[1]: int(order[2])})

for i in sorted(user_dict):
    print(f'\n{i}:')
    for i_i in sorted(user_dict[i]):
        print(f'\t{i_i}: {user_dict[i][i_i]}')
