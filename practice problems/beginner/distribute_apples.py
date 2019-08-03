t = int(input())

for _ in range(t):
    n,k = map(int, input().split())
    
    if k == 1 :
        print("NO")
        
   

    else :
       c = n // k
       if c % k == 0:
           print("NO")
       else:
            print("YES")
        
        
                
    """elif n // k == k:
        print("NO")
                  
    elif n // k < k:
        print("YES")"""
    
