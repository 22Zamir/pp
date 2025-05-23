## Цель практической работы
- Закрепить понятия «итератор» и «генератор», отработать использование методов iter и next.
- Отработать умение создавать классы-итераторы и функции-генераторы, генераторные выражения.
- Отработать использование аннотации типов.
## Что входит в задание
- Задача 1. Квадраты чисел.
- Задача 2. Пути файлов.
- Задача 3. Количество строк.
- Задача 4. Односвязный список.
- Задача 5. Обработка логов

## Задача 1. Квадраты чисел
### Что нужно сделать
Пользователь вводит число N. Напишите программу, которая генерирует последовательность из квадратов чисел от 1 до N (`1 ** 2`, `2 ** 2`, `3 ** 2` и так далее). Реализацию напишите тремя способами: класс-итератор, функция-генератор и генераторное выражение.
### Что оценивается
- Результат вычислений корректен.
- input содержит корректные приглашения для ввода. 
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
  - Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
  - Для создания нового класса на основе уже существующего используется наследование.
- Сообщения о процессе получения результата осмыслены и понятны для пользователя.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.

## Задача 2. Пути файлов
### Что нужно сделать
Реализуйте функцию `gen_files_path`, которая рекурсивно проходит по всем каталогам указанной директории (по умолчанию — корневой диск), находит указанный пользователем каталог и генерирует пути всех встреченных файлов. 

**Подсказка:**

Существует функция, которая может получать все имена файлов в дереве каталогов. Попробуйте найти ее самостоятельно.

### Что оценивается
- Результат вычислений корректен.
- Сообщения о процессе получения результата осмыслены и понятны для пользователя.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.

## Задача 3. Количество строк
### Что нужно сделать
Реализуйте функцию-генератор, которая берёт все питоновские файлы в директории и вычисляет количество строк в каждом файле, игнорируя пустые строки и строки комментариев. По итогу функция-генератор должна с помощью yield каждый раз возвращать количество строк в очередном файле. 
### Что оценивается
- Результат вычислений корректен.
- Input содержит корректные приглашения для ввода. 
- Сообщения о процессе получения результата осмыслены и понятны для пользователя.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.

## Задача 4. Односвязный список
### Что нужно сделать
Мы продолжаем тему структур данных и алгоритмов. И в этот раз вам нужно реализовать односвязный список.

Связный список — это структура данных, которая состоит из элементов, называющихся узлами. В узлах хранятся данные, а между собой узлы соединены связями. Связь — это ссылка на следующий или предыдущий элемент списка.

![](06_linked_list/linkedlist.PNG)

В односвязном списке связь — это ссылка только на следующий элемент, то есть в нём можно передвигаться только в сторону конца списка. Узнать адрес предыдущего элемента, опираясь на содержимое текущего узла, невозможно.

Реализуйте такую структуру данных без использования стандартных структур Python (list, dict, tuple и прочие) и дополнительных модулей. Для структуры реализуйте следующие методы:

- append — добавление элемента в конец списка;
- get — получение элемента по индексу;
- remove — удаление элемента по индексу.

Дополнительно: сделайте так, чтобы по списку можно было итерироваться с помощью цикла.

Пример основной программы:

```python
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
```

Результат:
```
Текущий список: [10 20 30]
Получение третьего элемента: 30
Удаление второго элемента.
Новый список: [10 30]
```
### Что оценивается
- Результат вычислений корректен.
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
  - Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
  - Для создания нового класса на основе уже существующего используется наследование.
- Формат вывода соответствует примеру.
- Переменные, функции и собственные методы классов имеют значащие имена (не `a`, `b`, `c`, `d`).
- Классы и методы/функции имеют прописанную документацию.
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.


## Задача 5. Обработка логов
### Контекст 
Вы работаете в большой компании, которая обслуживает сложную систему торговли. Каждый день генерируется огромное количество лог-файлов, содержащих информацию о торговых операциях. Вам поставлена задача разработать программу, которая будет автоматически анализировать эти лог-файлы и находить строки с сообщениями об ошибках (ERROR). Это поможет вам быстро отслеживать проблемы в торговой системе и эффективно на них реагировать.

### Задача 
Напишите программу, которая считывает строки из файла и выводит строки, содержащие слово ERROR, в новый файл. 

### Требования
- Используйте модуль os для работы с файлами и путями.
- Учтите, что файл может быть очень большим по объёму, поэтому не загружайте его в память целиком.
- Создайте функцию-генератор error_log_generator, которая будет получать на вход путь до файла с логами и возвращать строки из этого 
  файла, которые содержат слово ERROR (одно обращение к генератору должно возвращать одну строку из файла).


### Советы
- Цикл for по файлу будет считывать в память ровно по одной строке из файла за итерацию.
- Генератор должен возвращать только строки со словом ERROR. Другие строки, которые будут считываться из файла, нужно будет игнорировать 
  (применять yield только к правильным строкам).
- Для наглядного примера вы можете сгенерировать очень большой текстовый файл (для этого надо запустить код из файла text_generator.py) и 
  попробовать загрузить его в память при помощи метода read(), применённого к этому файлу. 
- Учтите, что генерация файла такого размера может занять несколько десятков минут!


## Что оценивается в практической работе
- Практическая работа сдана через GitLab.
- Структура папок и файлов репозитория соответствует репозиторию python_basic.
- Все задачи выполнены в соответствующих папках и файлах main.py.
- Описания коммитов осмыслены и понятны: `111`, `done`, `«я сделалъ»` — неверно, `added m15 homework`, `14.3 fix: variables naming` — верно.
- Использованы именованные индексы, не просто `i` (подробнее в видео 7.2).
- Использованы правильные числа, без дополнительных действий со стороны пользователя, без `+1` (подробнее об этом в видео 7.4).
- Правильно оформлен `input`, без пустого приветствия для ввода (подробнее об этом в видео 2.3).
- Переменные и функции имеют значащие имена, не только `a`, `b`, `c`, `d` (подробнее об этом в видео 2.3).
- Присутствуют пробелы после запятых и при бинарных операциях.
- Отсутствуют пробелы после имён функций и перед скобками: `print ()`, `input ()` — неверно, `print()` — верно.
- Правильно оформлены блоки `if-elif-else`, циклы и функции, отступы одинаковы во всех блоках одного уровня.
- Все входные и выходные файлы называются так, как указано в заданиях.
- Работа с файлами осуществляется с помощью контекстного менеджера `with`.
- Для обработки исключений используются блоки `try-excep`t.
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- При написании классов соблюдаются основные принципы ООП: инкапсуляция, наследование и полиморфизм.
  - Для получения и установки значений у приватных атрибутов используются сеттеры и геттеры.
  - Для создания нового класса на основе уже существующего используется наследование.
- Если классы вынесены в отдельный модуль, то импортируются определённые классы (запись вида `from garden import *` считается плохим тоном).
- Классы и методы/функции имеют прописанную документацию (хотя бы минимальную).
- Есть аннотация типов для методов/функций и их аргументов (кроме `args` и `kwargs`). Если функция/метод ничего не возвращает, то используется `None`.
## Советы и рекомендации
- [Подсказка по аннотации типов](https://docs.google.com/document/d/1Tm1dgEIYOYRJm9foU0fE0SgwhPg2zdn1hYxNRDsEBMM/edit).
- Арифметические операции [PEP8](https://docs.python.org/3.7/reference/expressions.html#operator-precedence) остаются в приоритете. Необходимо вводить and, or.
- Руководство по стилю Python [PEP8](https://www.python.org/dev/peps/pep-0008/) на английском языке.
- Руководство по стилю Python [PEP8](https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html) на русском языке.
- [Список встроенных функций](https://docs.python.org/3.7/library/functions.html).

## Как отправить практическую работу на проверку
Чтобы выполнить практическую работу, обновите репозиторий python_basic на своём компьютере при помощи IDE PyCharm. Задачи находятся в папке Module26.

Сдайте практические работы этого модуля через систему контроля версий Git сервиса Skillbox Gitlab. В видео с практической работой напишите «Сделано» и прикрепите ссылку на репозиторий. Ссылки на реплит оставлять не нужно.

