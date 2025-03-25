while True:
    user_password = input('Придумайте пароль: ')
    len_pass = len(user_password)
    shift_pass = len([x for x in user_password if x.isupper()])
    numbers = len([x for x in user_password if x.isdigit()])
    if (len_pass >= 8) and (shift_pass >= 1) and (numbers >= 3):
        print('Это надёжный пароль: ')
        break
    else:
        print('Пароль ненадёжный. Попробуйте еще раз.')

