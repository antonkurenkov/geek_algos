a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a > b > c or a < b < c:
    print('b')
elif b < a < c or b > a > c:
    print('a')
else:
    print('c')