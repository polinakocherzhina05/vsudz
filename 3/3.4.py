def f(x):
    while x:
        list.append(x)
        x = input("Ввод: ")
    lst = []
    print("Элемент | Частота")
    for t in list:
        if t not in lst:
            print(t, "|", list.count(t))
            lst.append(t)
x = input("Ввод: ")
list = []
f(x)