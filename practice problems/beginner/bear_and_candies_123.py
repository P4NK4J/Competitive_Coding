t = int(input())
for i in range(t):
    l, b = [int(x) for x in input().split()]
    temp = 1
    flag = 0
    while True:
        if l >= temp:
            l -= temp
        else:
            flag = "Bob"
            break
        temp += 1
        if b >= temp:
            b -= temp
        else:
            flag = "Limak"
            break
        temp += 1
    print(flag)
        
        
        
