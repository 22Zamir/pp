import family

parent = family.Parent('Вася Уткин', 55)
child_1 = family.Child('Маша', 12)
child_2 = family.Child('Петя', 11)
parent.add_child(child_1)
parent.add_child(child_2)
parent.calm()
parent.hungry()
parent.info()
