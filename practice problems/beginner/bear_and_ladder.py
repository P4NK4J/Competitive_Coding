t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    c = abs(n - k)
    if c == 2 and n%2 == 0 and k%2== 0:
        print("YES")
    elif c == 2 and n%2 != 0 and k%2 != 0:
        print("YES")
    elif n%2 != 0 and k%2 == 0 and c == 1 and n < k:
        print("YES")
    elif n%2 != 0 and k%2 == 0 and c == 1 and n > k:
        print("NO")
    elif n%2 != 0 and k%2 == 0 and c == 1:
        print("NO")
    elif c == 1 and k%2 != 0 and n%2 == 0 and n > k:
        print("YES")
    elif c == 1 and k%2 != 0 and n%2 == 0 and n < k:
        print("NO")
    else:
        print("NO")
    
    
    
