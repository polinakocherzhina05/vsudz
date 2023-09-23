X = float(input())
Y = float(input())
if X == 0 and Y != 0:
    print('Точка лежит на оси ординат')
elif Y == 0 and X != 0:
    print('Точка лежит на оси абцисс')
elif X > 0 and  Y > 0:
    print('Точка лежит в первой четверти')
elif X < 0 and Y > 0:
    print('Точка лежит во второй четверти')
elif X < 0 and Y < 0:
    print('Точка лежит в третей четверти')
elif X > 0 and Y < 0: 
    print('Точка лежит в четвертой четверти')
else:
    print('Точка лежит в начале координат')