t = int(input())

for _ in range(t):
    n = int(input())
    arr1 = [int(x) for x in input().split()]
    arr2 = [int(x) for x in input().split()]
    temp = [] * n

    for i in range(n):
        flag = arr1[i] * 20
        flag1 = arr2[i] * 10
        count = flag - flag1
        if count < 0:
            count = 0
        temp.append(count)
        flag1 = 0
        flag = 0
        count = 0
        maxi = max(temp)
    print(maxi)
         
