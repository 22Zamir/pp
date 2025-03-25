file = input('Введите названия файла: ')

if not file.endswith(('.txt', '.docx')):
    print('Ошибка: неверное расширение файла')
elif file.startswith(('@', '№', '$', '%', '^', '&', '*', '()')):
    print('Ошибка:недопустимый символ')
else:
    print('Файл назван верно')
