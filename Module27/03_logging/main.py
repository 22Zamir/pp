import datetime


def logging(func):
    def inner(*args, **kwargs):
        print(f'Название функции: {func.__name__}')
        print(f'Докумантация функции: {func.__doc__}')

        try:
            return func(*args, **kwargs)
        except Exception as e:
            with open('function_errors.log', 'a') as f:
                f.write(f'Название фунции: {func.__name__}')
                f.write(f'Дата и время: {datetime.datetime.now()}')
                f.write(f'Ошибка: {str(e)}')

    return inner


@logging
def my_func():
    return 2 * 4


@logging
def another_func():
    print('Hello world!')


functions = [my_func, another_func]
for func in functions:
    func()
