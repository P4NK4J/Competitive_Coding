n = int(input())
array = [int(x) for x in input().split()]
m = int(input())
alice = [int(x) for x in input().split()]
arr = []
x = array[0]
arr.append(x)

for i in range(1, n):
    if array[i] != x:
        arr.append(array[i])
        x = array[i]

l = len(arr)
rank = 0
temp = l-1

for i in range(m):
    if alice[i] < arr[-1]:
        rank = l + 1
    elif alice[i] == arr[-1]:
        rank = l
    elif alice[i] >= arr[0]:
        rank = 1
    else:
        for j in range(temp, -1, -1):
            if alice[i] < arr[j]:
                rank = j + 2
                break
            elif alice[i] == arr[j]:
                rank = j + 1
                break
            temp = j
    print(rank)
                
        
    
