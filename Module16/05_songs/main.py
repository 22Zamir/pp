violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

summ = 0
total_songs = int(input('Введите кол-во песен: '))


for i in range(total_songs):
    name_songs = input(f'Введите название {i + 1} песни')
    for song in range(len(violator_songs)):
        if violator_songs[song][0] == name_songs:
            summ += violator_songs[song][1]
print(f'\nОбщая продолжительность песен:{round(summ, 2)}минуты')
