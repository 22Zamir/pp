main_number = open('numbers.txt', 'r')
print('Содержимое файла numbers.txt')
summ_number = []
for i_number in main_number:
    print(i_number, end='')
    for i_i in i_number.split():
        summ_number.append(int(i_i))

total_summ = sum(summ_number)

summ_file = open('answer.txt', 'w')
summ_file.write(str(total_summ))
main_number.close()
summ_file.close()