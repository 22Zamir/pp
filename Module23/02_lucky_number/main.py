import random

def chance():
    result = False
    x = random.randint(1,13)
    if x == 13:
        result = True
    return result

sum_num = 0

with open('out_file.txt.', 'w') as file:
    while sum_num <= 777:
        try:
            number = int(input('Введите число: '))
            sum_num += number
            if chance() == True:
                raise Exception
            file.write(str(number) + '\n')
        except Exception:
            print('Вас достигла неудачи')
            break
    print('Вы успешно выполнили условие для выхода из порочного цикла!\n')
print('Содержимое файла out_file.txt')
with open('out_file.txt', 'r', encoding='utf-8') as final_file:
    lines = final_file.readlines()
    for line in lines:
        print(line)