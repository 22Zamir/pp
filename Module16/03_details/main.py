shop = [['каретка', 1200], ['седло', 300],
        ['педаль', 100], ['рама', 12000],
        ['обод', 2000], ['шатун', 200]]

user_details = input('Название детали: ')
count = 0
price_summ = 0

for i in range(len(shop)):
    if user_details in shop[i]:
        count += 1

if count >= 1:
    user_details_count = int(input('Введите кол-во: '))
else:
    print('Товар не найден.')
for _ in range(user_details_count):
    for i in range(len(shop)):
        if shop[i][0] == user_details:
            price_summ += shop[i][1]

print(price_summ)


