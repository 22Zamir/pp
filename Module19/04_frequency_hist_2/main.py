user_text = input('Введите текст: ')
text_dict = {}
text_dict_reversed = {}

for x in user_text:
    if x not in text_dict:
        text_dict[x] = 1
    else:
        text_dict[x] += 1

for key, value in text_dict.items():
    if value not in text_dict_reversed:
        text_dict_reversed[value] = [key]
    else:
        text_dict_reversed[value] += [key]

print(text_dict_reversed)