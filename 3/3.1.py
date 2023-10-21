def ff():
    x = input()
    lst = []
    while x:
        lst.append(x)
        x = input()
    return lst

print(ff())
