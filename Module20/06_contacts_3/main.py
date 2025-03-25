phone_book = {}

while True:
    main_menu = int(input('Введите номер действия:\n (1) - Добавить контакт \n (2) - Найти человека\n '))
    if main_menu == 1:
        name_surname = tuple(input('Введите ИМЯ и ФАМИЛИЮ нового контакта\n').title().split())
        if name_surname not in phone_book:
            number = int(input('Введите номер телефона:\n'))
            phone_book[name_surname] = number
            print(f'Текущий словарь контактов:{phone_book}')
        else:
            print(f'Такой человек уже есть в контактах.\nТекущий словарь контактов:{phone_book}')
    elif main_menu == 2:
        search = input('Введите фамилию для поиска:\n').title()
        for key, value in phone_book.items():
            if search == key[1]:
                print(key[0], key[1], value)
            else:
                print('Такого человека нет в контактах')
