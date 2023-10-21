from collections import Counter
from one import ff


def ff(x):
    print("Элемент | Частота")
    return Counter(x)
     
x = ff(input())
v = ff(x)
print(*[f'{i} | {v[i]}' for i in v] , sep = '\n') 
