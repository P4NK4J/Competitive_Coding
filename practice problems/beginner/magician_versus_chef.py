t = int(input())
for i in range(t):
    n,x,s = map(int, input().split())
    temp = [0] * (n+1)
    temp[x] = 1
    ctr = 0
    while ctr < s :
        a,b = map(int,input().split())
        c = 0
        c = temp[a]
        temp[a] = temp[b]
        temp[b] = c
        ctr += 1
    for i in range(len(temp)):
        if temp[i] == 1:
            print(i)
            break
