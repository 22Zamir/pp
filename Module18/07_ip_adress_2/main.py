ip = input('Введите строку IP: ').split('.')
if 4 > len(ip):
    print('Адрес - это четыре числа, разделённые точками')
else:
    count_num = 0
    for x in ip:
        if x.isdigit():
            if int(x) <= 255:
                count_num += 1
                continue
            else:
                print(f'{x} превышает 255')
        else:
            print(f'{x} не целое число')
            break
    if count_num == 4:
        print('IP-адрес корректен')