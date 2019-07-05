s = input()
t = input()
n = int(input())
fir = len(s)
sec = len(t)
count = 0
mini = min(fir, sec)

if fir + sec <= n :
    print("Yes")
else :
    for i in range(mini):
        if s[i] == t[i] :
            count += 1
        else :
            break
    d = fir - count
    e = sec - count
    sum = d + e
    #print(sum,count)
    if (sum + count) <= n:
        print("No")
    elif sum <= n :
        print("Yes")
    else :
        print("No")

    
    
