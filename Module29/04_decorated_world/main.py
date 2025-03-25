import functools


def decorator_with_args_any_decorator(func):
    def wrapped(*args, **kwargs):
        @functools.wraps(func)
        def wrapper(func):
            print(f'Переданные арги и кварги в декоратор {args, kwargs}')
            result = func
            return result

        return wrapper

    return wrapped


@decorator_with_args_any_decorator
def decorated_decorator(func):
    @functools.wraps(func)
    def wrapper(func):
        return func

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_func(text, num):
    print(f'Привет {text, num}')


decorated_func('User', 777)
