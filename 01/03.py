year = int(input('year = '))

if year % 4:
    intercalary = False
elif not year % 100 and year % 400:
    intercalary = False
else:
    intercalary = True

print(f'intercalary = {intercalary}')