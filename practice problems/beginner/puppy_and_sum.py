def Sum():
    d, n = map(int, input().split())
    for _ in range(d):
        n = n * (n + 1) / 2
    print(int(n))


n = int(input())
while n:
    Sum()
    n -= 1
