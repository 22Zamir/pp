## 7.4

1. Реализуйте собственный `StreamHandler`: в конструктор он должен принимать поток, с которым будет работать. Если такой не указан — берите `sys.stderr`.
2. Используйте этот обработчик вместо стандартного в конфигурационном файле из прошлой темы. 
3. Попробуйте при вызове какого-нибудь метода логирования передать по ключу `extra` словарь ещё с чем-нибудь. Например:

    ```python
    logger.debug('msg', extra={'very': 'much'})
    ```

    Теперь посмотрите, какие атрибуты есть у этого объекта `LogRecord`. Для этого рекомендуем воспользоваться функцией `vars(record)`.
        
    Как мы это можем использовать? Что будет, если эти атрибуты указать в строке-паттерне Formatter'а? Что будет, если их указать, но не передать в `extra`? 