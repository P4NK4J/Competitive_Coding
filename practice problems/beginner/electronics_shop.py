b,n,m = [int(x) for x in input().split()]
key = [int(x) for x in input().split()]
usb = [int(x) for x in input().split()]
l = list()

for i in range(n):
    sum = 0
    for j in range(m):    
        sum = key[i] + usb[j]
        if sum <= b :
            l.append(sum)

if len(l) != 0 :
    maxi = max(l)
    print(maxi)
else :
    print(-1)
    
