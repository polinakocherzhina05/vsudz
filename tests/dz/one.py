from gg.one1 import ff


def swap(pl, k):
    k %= len(pl)
    return pl[-k:] + pl[:-k]


 print(swap(ff(input()), int(input())))
