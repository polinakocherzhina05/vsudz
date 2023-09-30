x = int(input('Введите пятизначное число'))
while x >= 10000 and x <= 99999:
    print('Число не коректно для данной задачи')
    x = int(input('Введите пятизначное число:'))
x = str(x)
for a in x:
    print(a)
