films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorite_movie = []
user_check = int(input('Сколько фильмов хотите добавить?'))

for x in range(user_check):
    movie = input('Введите название фильма:')
    if movie in films:
        favorite_movie.append(movie)
    else:
        print('Такого фильма нет(((')
print(f'Ваши фльмы добавлены в список "Любимые" {favorite_movie}')
