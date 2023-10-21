from one import input_list
from collections import Counter
a = input_list()
a = Counter(a)
print("Элемент | Частота")
for i in a:
    print("{:7}".format(i), "|", a[i])
