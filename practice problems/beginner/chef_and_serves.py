t =  int(input())

for i in range(t):
    
    p1,p2,k = map(int, input().split())
    sum = p1 + p2
    sum = sum//k
    if sum % 2 == 0 :
        print("CHEF")
    else:
        print("COOK")
