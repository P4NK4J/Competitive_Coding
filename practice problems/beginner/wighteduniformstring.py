s =  input()
s = list(s)
n = int(input())
temp = []
temp2 = []
temp3 = []
sum = 0
flag = 1
for i in range(n):
    var = int(input())
    temp.append(var)
size = len(s)
for i in range(size):
    c = 0
    c = ord(s[i]) - 96
    temp2.append(c)
    #print(temp2)
l = len(temp2)
for i in range(l - 1):
    if temp2[i] == temp2[i+1]:
        sum = sum + temp2[i]
        temp3.append(sum)
    else:
        flag = 0
        temp3.append(sum+temp2[i])
        sum = 0

if len(temp2) == 1:
    temp3.append(temp2[0])
elif temp2[-1] == temp2[-2]:
    temp3.append(temp3[-1]+temp2[-1])
else:
    temp3.append(temp2[-1])
#print(temp3)
length = len(temp)
for i in range(length):
    if temp[i] in temp3:
        print("Yes")
    else:
        print("No")
        
    
        
