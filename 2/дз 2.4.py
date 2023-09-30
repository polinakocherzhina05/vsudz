x = input()
y, z = x.count('('), x.count(')')
if y > z:
    print(f'Не хватает {y - z} закрывающих скобок')
elif z > y:
    print(f'Не хватает {z - y} открывающих скобок')
else:
    print('Всё в порядке')
