n = int(input())
p = int(input())
count = 0
count2 = 0
flag = 0
temp = 0
for i in range(n):
    if i == p :
        break
    if i % 2 != 0:
        count += 1
    flag = 0
for i in range(n,-1,-1):
    if i == p :
        break
    if i % 2 == 0:
        count2 += 1
    temp = 0
mini = min(count,count2)
print(mini)
    
    
