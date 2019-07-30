def sumOfDigits(n):

    sum = 0
    while(n > 0):
        sum += n % 10 # n%10 gives the digit at units place
        n //= 10 # Integer division leads to loss of digit at unit's place, and shifts all digits by 1 place right.
    
    return sum 

t = int(input())

for k in range(t):

    n = int(input())
    arr = [int(x) for x in input().split()]
    ans = 0
    
    for i in range(n):
    
        for j in range(i+1,n):
        
            product = arr[i] * arr[j]
            sum = sumOfDigits(product)
            ans = max(ans, sum)
    print(ans)
        
    
    
