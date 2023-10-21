def f(x):
    while x:
        lst.append(x)
        x = input()
    return lst
x = input()
lst = []
print(f(x))
