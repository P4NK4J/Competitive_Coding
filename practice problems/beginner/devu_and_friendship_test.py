t = int(input())

for _ in range(t):

    n = int(input())
    arr = [int(x) for x in input().split()]
    maxi = max(arr)
    temp = [0] * (maxi + 1)  
    for i in arr:
        temp[i] += 1
        #print(temp)
    ans = n
    for j in range(len(temp)):
        flag = 1
        if temp[j] > 1 :
            ans = (ans - temp[j]) + 1
        #print(ans)
    print(ans)
            
