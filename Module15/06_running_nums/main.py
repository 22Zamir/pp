N = int(input('Сколько элементов будет в списке? '))
first_list = []
second_list = []
for x in range(N):
    element = (int(input(f'Введите {x + 1} элемент: ')))
    first_list.append(element)

step = int(input('Сдвиг:'))
for i in range(N):
    new_place = first_list[i - step]
    second_list.append(new_place)
print(f'Изначальный список:{first_list}\nСдвинутый список:{second_list}')
