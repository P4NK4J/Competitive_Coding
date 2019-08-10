t = int(input())
for _ in range(t):
    s = input()
    s = list(s)
    temp = [0] * 123
    for i in range(len(s)):
        s[i] = ord(s[i])

    for i in s:
        temp[i] += 1    
    total  = sum(temp)
    for i in range(len(temp)):
        flag = " "
        if temp[i] == total - temp[i]:
            flag = "YES"
            break
        else:
            flag = "NO"
    total = 0
    print(flag)
        
                   
    
    
