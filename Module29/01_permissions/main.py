def check_permission(user_name):
    def check_permission_2(func):

        def wrapped(*args, **kwargs):
            try:
                if user_name in admin:
                    return func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print(f'PermissionError: У пользователья недостаточно прав, чтобы выполнить фунцию {func.__name__}')
        return wrapped

    return check_permission_2


admin = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('ssss')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
