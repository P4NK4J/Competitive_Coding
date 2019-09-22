t = int(input())
for i in range(t):
    n = int(input())
    xen = [int(x) for x in input().split()]
    yan = [int(x) for x in input().split()]
    c = 0
    d = 0
    for i in range(n):
        if i % 2 == 0:
            c += xen[i]
        else :
            c += yan[i]
    
    for j in range(n):
        if j % 2 == 0:
            d += yan[j]
        else:
            d += xen[j]
    #print(c,d)

    mini = min(c,d)
    print(mini)
