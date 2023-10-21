def ff(x):
    lst = []
    while x:
        lst.append(x)
        x = input()
    return lst
x = input()
print(ff(x))
