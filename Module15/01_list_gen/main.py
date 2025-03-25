number = int(input('Введите число: '))
number_list = []

for x in range(1, number + 1):
    if x % 2 == 1:
        number_list.append(x)
print(number_list)
