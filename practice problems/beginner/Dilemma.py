t = int(input())
for _ in range(t):
    s = input()
    s = [int(i) for i in s]

    temp = [0] * (len(s) + 1)

    for i in s:
        temp[i] += 1

    if temp[1] % 2 != 0:
        print("WIN")

    else:
        print("LOSE")
            
                
            
        
