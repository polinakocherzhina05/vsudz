a = [int(a) for a in input().split() ]
def f(a):
    return sum(a) / len(a)
print(f(a))