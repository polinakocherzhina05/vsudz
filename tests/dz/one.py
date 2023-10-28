from gg.one1 import ff


def swap(pl, k):
    k %= len(pl)
    return pl[-k:] + pl[:-k]


if __name__ == "__main__":
    print(swap(ff(input()), int(input())))
