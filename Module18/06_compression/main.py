s = 'aaaAAbbcaaaA'
s2 = []
n = 1

for i in range(len(s)):
    if s[i] == s[i + 1:i + 2]:
        n += 1
        continue
    s2.append(''.join([s[i], str(n)]))
    n = 1
print(f'Закодированная строка: {''.join(s2)}')

