import collections
s = input()
s = list(s)
lis = collections.Counter(s)
#print(lis)
if len(s)%2 == 0:
    flag = True
    for i in lis.keys():
        if lis[i] % 2 != 0:
            flag = False
            break
else:
    flag = True
    flag2 = True
    for i in lis.keys():
        if lis[i] % 2 != 0 and flag2:
            flag2 = False
        elif lis[i] % 2 != 0 and not flag2:
            flag = False
            break

if flag:
    print("YES")
else:
    print("NO")
        
