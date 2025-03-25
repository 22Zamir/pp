user = 'dss dddds zamir'
maxWord = ''
word = ''
for i in range(len(user)):
    if user[i] == ' ':
        if len(word) > len(maxWord):
            maxWord = word
        word = ''
    else:
        word += user[i]
print(maxWord)