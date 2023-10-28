def f(a):
    return sum(a) / len(a)


a = [int(a) for a in input().split()]
print(f(a))