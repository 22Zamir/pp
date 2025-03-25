class Student:

    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades

    def averaga(self):
        return sum(self.grades) / len(self.grades)


students = []

for i in range(10):
    name = input('Введите ФИ студента: ')
    group = int(input('Введите номер группы: '))
    grades = []
    for x in range(5):
        grade = float(input('Введите успеваемость: (0-5)'))
        grades.append(grade)
        student = Student(name, group, grades)
        students.append(student)

sorted_student = sorted(students)