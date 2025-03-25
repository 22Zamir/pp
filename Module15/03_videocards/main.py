old_list = []
new_list = []
kol_vo = int(input('Введите кол-во видеокарт:'))

for x in range(1, kol_vo + 1):
    video_card = int(input(f'Введите {x} видекарту:'))
    old_list.append(x)
print(old_list)
