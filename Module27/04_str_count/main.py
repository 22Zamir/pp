def counter(func):
    def wrapped(*args, **kwargs):
        wrapped.count += 1
        print(f'Функция {func.__name__} была вызвана  {wrapped.count} раз(а)')
        return func(*args, **kwargs)

    wrapped.count = 0
    return wrapped


@counter
def test():
    print('Hello world')


test()
test()
