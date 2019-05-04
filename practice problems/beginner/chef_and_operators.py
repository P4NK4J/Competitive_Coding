n =  int(input())
lis = []
lis2 = []
for i in range(n):
    x = [int (x) for x in input().split()]
    lis.append(x)
    if lis[i][0] < lis[i][1]:
        c = "<"
        lis2.append(c)
    elif lis[i][0] > lis[i][1]:
        c = ">"
        lis2.append(c)
    elif lis[i][0] == lis[i][1]:
        c = "="
        lis2.append(c)
for i in range(n):
    print(lis2[i])
