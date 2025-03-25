num_list = []
N = int(input('Сколько будет чисел в списке? '))

for x in range(N):
    num = int(input('Введите число: '))
    num_list.append(num)

for _ in range(len(num_list) - 1):
    for i in range(len(num_list) - 1):
        print(f'Сравнивниваем числа... ({num_list[i]} c {num_list[i + 1]})')
        if num_list[i] > num_list[i + 1]:
            num_list[i], num_list[i + 1] = num_list[i + 1], num_list[i]
            print(num_list)

print(num_list)
