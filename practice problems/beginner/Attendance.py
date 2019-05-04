t =  int(input())
for _ in range(t):
    m  = int(input())
    lis = []
    lis2 = []
    temp = [0] * m
    for i in range(m):
        s = input().split()
        lis.append(s)
    for i in range(m):
        for j in range(i+1,m):
            if lis[i][0] == lis[j][0]:
                temp[i] = 1
                temp[j] = 1
                break
        if temp[i] == 0:
            lis2.append(lis[i][0])
        else:
            lis2.append(lis[i][0] + " " + lis[i][1])
    
    for i in range(m):
        print(lis2[i])

