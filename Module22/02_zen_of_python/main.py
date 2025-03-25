file = open('zen.txt', 'r')
print('\n'.join(file.read().splitlines()[::-1]))
file.close()