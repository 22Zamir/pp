## 7.2

1. Создайте следующую цепочку логеров:
    ```
    |-- root
    |   |-- sub_1 (INFO)
    |   |-- sub_2
    |   |   |-- sub_sub_1 (DEBUG)
    ```

2. Добавьте для логгеров `sub_1` и `sub_sub_1` обработчик (один на всех) с уровнем `DEBUG`. Установить уровень на обработчик можно точно так же как и на сам логгер — через `setLevel`.

3. Создайте Formatter, который бы делал сообщения вида:
   `<имя логера> || <уровень> || <сообщение> || <модуль>.<имя функции>:<номер строки>`

   и добавьте его к созданному ранее обработчику.

4. Создайте для логгера обработчик `root` с уровнем `DEBUG` и уже созданным Formatter.

5. Сделайте так, чтобы сообщения из цепочки логгера `sub_2` не обрабатывались логгером `root`, а из `sub_1` наоборот продолжили бы выводиться.