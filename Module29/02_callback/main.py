def callback(url):
    def decorator(func):
        def wrapper():
            print(f'вызов фунции {func.__name__}, обрабатывающей запрос по адресу {url} ')
            answer = func()
            print(f'Ответ сервера: {answer}')
            return answer
        return wrapper
    return decorator



@callback('//')
def example():
    print('Пример фунции которая возращает ответ сервера')
    return 'OK'


rout = '//'

if rout == '//':
    answer = example()
    print(f'Ответ:{answer}')
else:
    print('такого пути нет ')
