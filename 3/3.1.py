def f(x):
    while x:
        list.append(x)
        x = input()
    return list
x = input()
list = []
print(f(x))