def is_palindrom(num_list):
    reversed_list = []
    for i_num in range(len(num_list) -1, -1, -1):
        reversed_list.append(num_list[i_num])
    if num_list == reversed_list:
        return True
    else:
        return False

nums = [1, 2, 3, 4, 5]
new_nums = []
answer = []

for i_nums in range(0, len(nums)):
    for j_elem in range(i_nums, len(nums)):
        new_nums.append(nums[j_elem])
    if is_palindrom(new_nums):
        for i_answer in range(0, i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []
print(f'Исходный список {nums}\nНужно чисел для паллиндрома: {len(nums)}\nСписок чисел{answer}')