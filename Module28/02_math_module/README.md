## Задача 2. Математический модуль
### Что нужно сделать
Вася использует в своей программе очень много различных математических вычислений, связанных с фигурами. Например, нахождение их площадей или периметров. Поэтому, чтобы не захламлять код огромным количеством функций, он решил выделить для них отдельный класс, подключить как модуль и использовать по аналогии с модулем `math`.

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

