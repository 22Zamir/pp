summ = 0
count = 0
try:
    with open('people.txt', 'r', encoding='utf-8') as people:
        for i_line in people:
            try:
                lenght = len(i_line)
                count += 1
                if i_line.endswith('\n'):
                    lenght -= 1
                if lenght < 3:
                    raise ValueError(f'Ошибка: менее стрех символов встроке: {count}')
                summ += lenght
            except ValueError:
                print(f'Ошибка: менее стрех символов встроке: {count}')
finally:
    print(f'Общее кол-во символов - {summ}')