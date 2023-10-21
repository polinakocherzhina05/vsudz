def f(x):
    while x:
        lst.append(x)
        x = input("Ввод: ")
    lst = []
    print("Элемент | Частота")
    for t in lst:
        if t not in lst:
            print(t, "|", lst.count(t))
            lst.append(t)
x = input("Ввод: ")
lst = []
f(x)
