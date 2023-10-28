from one import ff
from collections import Counter


a = ff()
a = Counter(a)
print("Элемент | Частота")
for i in a:
    print(f'{i} | {a[i]}')