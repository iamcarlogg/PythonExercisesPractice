def lessThan(num):
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for x in a:
        if x>num:
            print(x)
            b.extend(int(x))
    print(b)
lessThan(10)