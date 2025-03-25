import random

first_team = [round((random.uniform(7, 10)), 2) for x in range(20)]
second_team = [round((random.uniform(7, 10)), 2) for x in range(20)]
win_team = []

for x in range(20):
    if first_team[x] >= second_team[x]:
        win_team.append(first_team[x])
    else:
        win_team.append(second_team[x])
print(f'Первая команда:{first_team}\nВторая команда:{second_team}\nПобедитель тура:{win_team}')
