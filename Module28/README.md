## Цели практической работы
Отработать: 

- применение множественного наследования, закрепить понимание порядка разрешения методов в Python;
- создание и применение примесей и абстрактных классов;
- применение декораторов `setter` и `property`, а также `classmethod` для более правильного и чистого кода.
## Что входит в работу
- Задача 1. Работа с файлом 2.
- Задача 2. Математический модуль.
- Задача 3. Дата.
- Задача 4. Кэширование запросов

## Задача 1. Работа с файлом 2
### Что нужно сделать
Реализуйте модернизированную версию контекст-менеджера File: 

- теперь при попытке открыть несуществующий файл менеджер автоматически создаёт и открывает этот файл в режиме записи; 
- на выходе из менеджера подавляются все исключения, связанные с файлами.
### Что оценивается
- Результат вычислений корректен.
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
  - Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры с соответствующими декораторами.
  - Для создания нового класса на основе уже существующего используется наследование.
  - Для статических и классовых методов используется декоратор `classmethod`.
- Сообщения о процессе получения результата осмысленны и понятны для пользователя.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращают, то используется `None`.
## Задача 2. Математический модуль
### Что нужно сделать
Ирина использует в своей программе очень много различных математических вычислений, связанных с фигурами. Например, нахождение их площадей или периметров. Поэтому, чтобы не захламлять код огромным количеством функций, она решила выделить для них отдельный класс, подключить как модуль и использовать по аналогии с модулем `math`.

Реализуйте класс `MyMath`, состоящий как минимум из следующих методов (можете бонусом добавить и другие методы):

- вычисление длины окружности,
- вычисление площади окружности,
- вычисление объёма куба,
- вычисление площади поверхности сферы.

Пример основного кода:
```python
res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
```

Результат:
```
31.41592653589793
113.09733552923255
```
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

## Задача 3. Дата
### Что нужно сделать
Реализуйте класс `Date`, который должен:

- проверять числа даты на корректность;
- конвертировать строку даты в объект класса `Date`, состоящий из соответствующих числовых значений дня, месяца и года.

Оба метода должны получать на вход строку вида `dd-mm-yyyy`.

При тестировании программы объект класса Date должен инициализироваться исключительно через метод конвертации, например:

```python
date = Date.from_string('10-12-2077')
```

Неверный вариант: `date = Date(10, 12, 2077)`

Пример основного кода:
```python
date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
```

Результат:
```
День: 10	Месяц: 12	Год: 2077
True
False
```
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


## Задача 4. Кэширование запросов

### Контекст 
Вы разрабатываете программу для кэширования запросов к внешнему API. Часто повторяющиеся запросы занимают много времени, поэтому вы решаете создать класс LRU Cache (Least Recently Used Cache), который будет хранить ограниченное количество запросов и автоматически удалять самые старые при достижении лимита. Это позволит значительно ускорить повторяющиеся запросы, так как данные будут браться из кэша, а не отправляться повторно.

### Задача
1) Создайте класс LRU Cache, который хранит ограниченное количество объектов и, при превышении лимита, удаляет самые давние (самые старые) 
использованные элементы. 
2) Реализуйте методы добавления и извлечения элементов с использованием декораторов property и setter.    
    ```
    @property
    def cache(self): # этот метод должен возвращать самый старый элемент
        ...
    @cache.setter
    def cache(self, new_elem): # этот метод должен добавлять новый элемент
        ...
    ```

### Советы
Не забывайте обновлять порядок использованных элементов. В итоге должны удаляться давно использованные элементы, а не  давно добавленные, так как давно добавленный элемент может быть популярен, и его удаление не поможет ускорить новые запросы.

Пример:
```
# Создаём экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)


# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")


# # Выводим текущий кэш
cache.print_cache() # key1 : value1, key2 : value2, key3 : value3


# Получаем значение по ключу
print(cache.get("key2")) # value2


# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")


# Выводим обновлённый кэш
cache.print_cache() # key2 : value2, key3 : value3, key4 : value4



Ожидаемый вывод в консоли:

LRU Cache:
key1 : value1
key2 : value2
key3 : value3

value2

LRU Cache:
key3 : value3
key2 : value2
key4 : value4
```


## Что оценивается в практической работе
- Практическая работа сдана через GitLab.
- Структура папок и файлов репозитория соответствует репозиторию python_basic.
- Все задачи выполнены в соответствующих папках и файлах `main.py`.
- Описания коммитов осмысленны и понятны: `111`, `done`, `«я сделалъ»` — неверно; `added m15 homework`, `14.3 fix: variables naming` — верно.
- Использованы именованные индексы, не просто `i` (подробнее в видео 7.2).
- Использованы правильные числа, без дополнительных действий со стороны пользователя, без `+`1 (подробнее об этом в видео 7.4).
- Правильно оформлен input, без пустого приветствия для ввода (подробнее об этом в видео 2.3).
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
Чтобы выполнить практическую работу, обновите репозиторий python_basic на своём компьютере при помощи IDE PyCharm. Задачи находятся в папке Module28.

Сдайте практические работы этого модуля через систему контроля версий Git сервиса Skillbox GitLab. В материалах с практической работой напишите «Сделано» и прикрепите ссылку на репозиторий. Ссылки на реплит оставлять не нужно.

