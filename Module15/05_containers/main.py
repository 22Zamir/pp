count = int(input('Введите кол-во контейнеров: '))
cant_list = []
for x in range(count):
    ces_cant = int(input(f'Введите вес {x + 1} контейнера: '))
    if ces_cant < 200:
        cant_list.append(ces_cant)


new_cant = int(input('Введите вес нового контейнера: '))
index = 0
while index < len(cant_list) and cant_list[index] >= new_cant:
    index += 1

print(index)
# Здесь  проблема
