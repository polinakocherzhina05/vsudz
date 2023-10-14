def f(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    print(' '.join(str(x) for x in fib[:n]))
n = int(input("Введите количество чисел Фибоначчи: "))
f(n)