def ff():
    x = input()
    lst = []
    while x:
        lst.append(x)
        x = input()
    return lst

if __name__ == '__main__':
    print(ff())
