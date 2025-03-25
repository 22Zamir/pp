def how_are_you(func):
    def wrapped(*args, **kwargs):
        print('Как дела?')
        input('')
        print('А у меня не очень! Ладно, держи свою функцию.')
        return func(*args, **kwargs)
    return wrapped


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()
