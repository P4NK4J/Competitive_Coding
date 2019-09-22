t = int(input())
for i in range(t):
    n,k = map(int, input().split())
    lis = [int(x) for x in input().split()]
    lis.sort(reverse = True)
    limit = lis[k-1]
    count = 0
    for i in range(n):
        if lis[i] >= limit:
            count += 1
    print(count)
