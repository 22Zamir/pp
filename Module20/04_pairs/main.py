import random

random_list = ([random.randint(0, 10) for _ in range(10)])
new_list = []
zip_list = zip(random_list[::2], random_list[1::2])

for i in zip_list:
    new_list.append(i)

print(f'Оригинальный список:{random_list}')
print(f'Новый список:{new_list}')
######################################################################################################################
######################################################################################################################
print('-' * 60)
######################################################################################################################
######################################################################################################################

random_list_second = ([random.randint(0, 10) for _ in range(10)])
num_list = [(random_list_second[i], random_list_second[i + 1]) for i, j in enumerate(random_list_second) if i % 2 == 0]
print(f'Оригинальный список:{random_list_second}')
print(f'Новый список:{num_list}')
