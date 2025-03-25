import os
import re


def count_lines_in_python(directory):
    # Получаем список файлов
    files = [f for f in os.listdir(directory) if f.endswith('.py')]

    for file_name in files:
        with open(os.path.join(directory, file_name), 'r') as file:
            total_lines = 0

            # ПРОВЕРКА
            for line in file:
                # ПУСТЫКЕ СТРОКИ НЕ БЕРЕМ
                if not line.strip():
                    continue
                    # ПРОВЕКА НА КОММЕНТ
                if line.strip().startswith('#'):
                    continue
            yield f'{file_name}: {total_lines}'


dir_path = 'C:/'
for result in count_lines_in_python(dir_path):
    print(result)
