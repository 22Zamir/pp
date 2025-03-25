students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

print('Список пар "ID студента — возраст": {age}'.format(age=[(id, students[id]['age']) for id in students]))


def interesting_and_len(dict):
    return set(sum([dict.get(i).get('interests') for i in dict], [])), sum(len(dict[i]['surname']) for i in dict)


interesting, surname_len = interesting_and_len(students)
print(f'Полный список интересов всех студентов: {interesting} \n' 
f'Общая длина всех фамилий студентов: {surname_len}')
