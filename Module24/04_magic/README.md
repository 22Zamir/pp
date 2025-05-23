## Задача 4. Магия
### Что нужно сделать
Для одной игры необходимо реализовать механику магии, где при соединении двух элементов получается новый. У нас есть четыре базовых элемента: «Вода», «Воздух», «Огонь», «Земля». Из них как раз и получаются новые: «Шторм», «Пар», «Грязь», «Молния», «Пыль», «Лава».

Вот таблица преобразований:

- Вода + Воздух = Шторм;
- Вода + Огонь = Пар;
- Вода + Земля = Грязь;
- Воздух + Огонь = Молния;
- Воздух + Земля = Пыль;
- Огонь + Земля = Лава.

Напишите программу, которая реализует все эти элементы. Каждый элемент необходимо организовать как отдельный класс. Если результат не определён, то возвращается `None`.

Примечание: сложение объектов можно реализовывать через магический метод `__add__`, вот пример использования:

```python
class Example_1:
    def __add__(self, other):
        return Example_2()

class Example_2:
    answer = 'сложили два класса и вывели'

a = Example_1()
b = Example_2()
c = a + b
print(c.answer)
```

Дополнительно: придумайте свой элемент (или элементы), а также реализуйте его взаимодействие с остальными.
### Что оценивается
- Результат вычислений корректен.
- Модели реализованы в стиле ООП, основной функционал описан в методах классов и в отдельных функциях.
- Переменные, функции и собственные методы классов имеют значащие имена, не `a`, `b`, `c`, `d`.

