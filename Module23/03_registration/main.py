def answer(file_str):
    name, mail, age = file_str.split(' ')
    symbol = ('@', '.')
    age = int(age)
    if name.isalpha() is False:
        raise NameError('Поле «Имя» содержит НЕ только буквы:')
    elif age not in range(10, 100):
        raise ValueError('Поле «Возраст» НЕ представляет число от 10 до 99:')
    else:
        for char in symbol:
            if char not in mail:
                raise SyntaxError('Поле «Имейл» НЕ содержит @ и точку:')
    return file_str


with open('registrations.txt', 'r', encoding='utf-8') as file, \
        open('registrations_bad.txt', 'w', encoding='utf-8') as error, \
        open('registrations.txt_good', 'w', encoding='utf-8') as good:
    for str_in_file in file:
        print(str_in_file, end='')
        try:
            str_file = answer(str_in_file)
        except (NameError, ValueError, SyntaxError) as err:
            error.write('\n' + str_in_file + str(err) + '\n')
        else:
            good.write(str_in_file + '\n')
