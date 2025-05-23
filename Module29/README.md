## Цели практической работы
Отработать: 

- создание и использование декораторов, принимающие аргументы, использование вложенных декораторов;
- декорирование классов, особенности декорирования классов, модификацию поведения внутри класса с помощью специальных функций.
## Что входит в работу
- Задача 1. Права доступа.
- Задача 2. Функция обратного вызова.
- Задача 3. Логирование в формате.
- Задача 4. Весь мир — декоратор…
- Задача 5. Синглтон.
- Задача 6. Класс-декоратор

## Задача 1. Права доступа
### Что нужно сделать
На вас возложили задачу по созданию и поддержке специализированного сайта-форума. Вы только начали выполнять задачу и сейчас остановились на реализации действий, которые могут совершать посетители форума. И конечно же, для разных пользователей прописаны разные возможности.

Напишите декоратор `check_permission`, который проверяет, есть ли у пользователя доступ к вызываемой функции, и если нет, то выдаёт исключение `PermissionError`.

Пример кода:
```python
user_permissions = ['admin']

@check_permission('admin')
def delete_site():
    print('Удаляем сайт')

@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
```
Результат:
```
Удаляем сайт
PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию add_comment
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращают, то используется `None`.

## Задача 2. Функция обратного вызова
### Что нужно сделать
При работе с сетью и веб-сервисами иногда используется функция `callback`, так называемая функция обратного вызова. Это функция, которая вызывается при срабатывании определённого события (переходе на страницу, получении сообщения или окончании обработки процессором). В неё можно передать функцию, чтобы она выполнилась после определённого события. Это используется, например, в HTTP-серверах в ответ на URL-запросы. Реализуйте такую функцию.

Пример функции:
```python
@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'
```
Основной код:
```python
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

```
Ожидаемый результат:
```
Пример функции, которая возвращает ответ сервера
Ответ: OK
```
**Подсказка:** функция `callback` может быть вызвана следующим действием в зависимости от условия или просто так.
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращают, то используется `None`.

## Задача 3. Логирование в формате
### Что нужно сделать
Реализуйте декоратор, который будет логировать все методы декорируемого класса (кроме магических методов) и в который можно передавать формат вывода даты и времени логирования.

Пример кода, передаётся формат `«Месяц День Год - Часы Минуты Секунды»`: 
```python
@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
```
Результат:
```
- Запускается 'B.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37 
- Запускается 'A.test_sum_1'. Дата и время запуска: Apr 23 2021 - 21:50:37 
Тут метод test_sum_1
- Завершение 'A.test_sum_1', время работы = 0.187s 
Тут метод test_sum_1 у наследника
- Завершение 'B.test_sum_1', время работы = 0.187s 
- Запускается 'B.test_sum_2'. Дата и время запуска: Apr 23 2021 - 21:50:37 
Тут метод test_sum_2 у наследника
- Завершение 'B.test_sum_2', время работы = 0.370s
```
**Совет:** внимательно пересмотрите видео 29.4, если сталкиваетесь с трудностями при решении этой задачи.
### Что оценивается
- Результат вычислений корректен.
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
  - Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры с соответствующими декораторами.
  - Для создания нового класса на основе уже существующего используется наследование.
  - Для статических и классовых методов используется декоратор `classmethod`.
- Формат вывода соответствует примеру.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращают, то используется `None`.

## Задача 4. Весь мир — декоратор…
### Что нужно сделать
Реализуйте декоратор для декораторов: он должен декорировать другую функцию, которая должна быть декоратором, и даёт возможность любому декоратору принимать произвольные аргументы.

Пример использования:

```python
@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):... # отсюда уже сами!


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)
```

Результат:
```
Переданные арги и кварги в декоратор: (100, 'рублей', 200, 'друзей') {}
Привет, Юзер 101
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращают, то используется `None`.

## Задача 5. Синглтон
### Что нужно сделать
Синглтон — это порождающий паттерн проектирования, который гарантирует, что у класса есть только один экземпляр, и предоставляет к нему глобальную точку доступа. Синглтонами мы уже пользовались, к ним относятся, например, `None`, `True` и `False`. Именно потому, что `None` является синглтоном, мы можем использовать оператор `is` — он возвращает `True` только для объектов, представляющих одну и ту же сущность.

Реализуйте декоратор `singleton`, который превращает класс в одноэлементный. То есть при множественной инициализации объекта этого класса будет сохранён только первый инстанс, а все остальные попытки создания будут возвращать первый экземпляр.

Пример кода:

```python
@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
```

Результат:
```
1986890616688
1986890616688
True
```
### Что оценивается
- Результат вычислений корректен.
- Формат вывода соответствует примеру.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращают, то используется `None`.


## Задача 6. Класс-декоратор

### Контекст 
Вы работаете в компании, которая разрабатывает программное обеспечение для финансовых анализов. Одна из ключевых задач в вашей работе — реализация сложного алгоритма для прогнозирования финансовых показателей. Этот алгоритм требует множества вычислений и может занимать длительное время. 
Вам поставлена задача создать декоратор, который будет логировать аргументы, результаты и время выполнения этой функции. Это поможет отслеживать прогресс выполнения алгоритма и анализировать его производительность.

### Задача 
Создайте декоратор, который логирует аргументы, результаты и время выполнения функции. 
Реализуйте декоратор как класс и примените его к функции complex_algorithm. Запустите задекорированную функцию и проверьте время её выполнения.
```
# Замерить время выполнения кода можно при помощи модуля time:
import time


start_time = time.time()  # Записываем время до вычислений
# ...вычисления...
end_time = time.time()  # Затем записываем время после вычислений
execution_time = end_time - start_time  # Их разница будет временем выполнения кода вычислений


# Пример:
@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется “сложный” алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    # Можете попробовать вынести создание файла из циклов и проверить, сколько времени алгоритм будет работать в этом случае
    return result
    
# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)


# Вывод в консоли:
Вызов функции complex_algorithm
Аргументы: (10, 50), {}
Результат: 14500
Время выполнения: 0.20143938064575195 секунд

```

### Советы
- Вспомните пример работы с классом-декоратором из видео «Декоратор как класс».
- Чтобы получить имя функции, используйте атрибут __name__: func.__name__


## Что оценивается в практической работе
- Практическая работа сдана через GitLab.
- Структура папок и файлов репозитория соответствует репозиторию python_basic.
- Все задачи выполнены в соответствующих папках и файлах `main.py`.
- Описания коммитов осмысленны и понятны: `111`, `done`, `«я сделалъ»` — неверно; `added m15 homework`, `14.3 fix: variables naming` — верно.
- Использованы именованные индексы, не просто `i` (подробнее в видео 7.2).
- Использованы правильные числа, без дополнительных действий со стороны пользователя, без `+1` (подробнее об этом в видео 7.4).
- Правильно оформлен `input`, без пустого приветствия для ввода (подробнее об этом в видео 2.3).
- Переменные и функции имеют значащие имена, не только `a`, `b`, `c`, `d` (подробнее об этом в видео 2.3).
- Есть пробелы после запятых и при бинарных операциях.
- Нет пробелов после имён функций и перед скобками: `print ()`, `input ()` — неверно; `print()` — верно.
- Правильно оформлены блоки `if-elif-else`, циклы и функции; отступы одинаковы во всех блоках одного уровня.
- Все входные и выходные файлы называются так, как указано в заданиях.
- Работа с файлами осуществляется с помощью контекстного менеджера `with`.
- Для обработки исключений используются блоки `try-except`.
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
  - Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры с соответствующими декораторами.
  - Для создания нового класса на основе уже существующего используется наследование.
  - Для статических и классовых методов используется декоратор `classmethod`.
- Если классы вынесены в отдельный модуль, то импортируются определённые классы (запись вида `from garden import *` считается плохим тоном).
- Классы и методы/функции имеют прописанную документацию (хотя бы минимальную).
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращают, то используется `None`.
- Во всех декораторах используется `functools.wraps`.
## Рекомендации
- Арифметические операции [PEP8](https://docs.python.org/3.7/reference/expressions.html#operator-precedence) остаются в приоритете. Необходимо вводить and, or.
- Руководство по стилю Python [PEP8](https://www.python.org/dev/peps/pep-0008/) на английском языке.
- Руководство по стилю Python [PEP8](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html) на русском языке.
- [Список встроенных функций](https://docs.python.org/3.7/library/functions.html).
## Как отправить работу на проверку
Чтобы выполнить практическую работу, обновите репозиторий python_basic на своём компьютере при помощи IDE PyCharm. Задачи находятся в папке Module29.

Сдайте практические работы этого модуля через систему контроля версий Git сервиса Skillbox GitLab. В материалах с практической работой напишите «Сделано» и прикрепите ссылку на репозиторий. Ссылки на реплит оставлять не нужно.

