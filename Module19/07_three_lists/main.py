array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

array_1_set = set(array_1)
array_2_set = set(array_2)
array_3_set = set(array_3)

result_1 = [num for num in [i for i in array_1 if i in array_2] if num in array_3]
result_2 = [num for num in [i for i in array_1 if i not in array_2] if num not in array_3]

print(f'Решение без множеств:\n {result_1}')
print(f'С использованием мнжеств.\n {array_1_set & array_2_set & array_3_set}')

print(f'Решение без множеств:\n {result_2}')
print(f'С использованием мнжеств.\n {array_1_set - array_2_set - array_3_set}')
