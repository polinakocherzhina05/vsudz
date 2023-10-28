def cn(n):
    if n < 2:
        return 1
    return n * cn(n - 1)


if __name__ == "__main__":
    print(cn(int(input())))