count = int(input('Введите количество пар слов: '))
text_dict = {}
for i in range(1, count + 1):
    user_text = input(f'{i} - пара: ').lower().split('-')
    print(user_text)
    text_dict[user_text[0]] = user_text[1]
    text_dict[user_text[1]] = user_text[0]
    print(text_dict)

