letters = "аоиеёэыуюя"

text = input('Введите текст: ')

user = [x for x in text if x in letters]

print(f'Гласные буквы:{user}\nДлинна:{len(letters)}')