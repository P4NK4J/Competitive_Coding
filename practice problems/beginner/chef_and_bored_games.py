for _ in range(int(input())):
    n, c = int(input()), 0
    s = n+1
    for x in range(1, s, 2):
        c += n*n
        n -= 2
    print(c)
