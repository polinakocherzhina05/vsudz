def notsame(x) -> bool:
    x = [(i, type(i)) for i in x]
    return len(x) == len(set(x))


if __name__ == "__main__":
    print(notsame(input().split()))