guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    user = input('Гость пришёл или ушёл?')
    if user == 'пришел':
        user_guests = input('Кто пришел?')
        if len(guests) >= 6:
            print(f'Прости, {user_guests}, но мест нет')
        else:
            guests.append(user_guests)
            print(f'Привет, {user_guests}!')
    elif user == 'ушел':
        guests.remove(input('Кто ушел?'))
    else:
        print('Вечеринка закончилась, все легли спать')
        break
