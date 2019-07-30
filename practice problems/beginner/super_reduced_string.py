<<<<<<< HEAD
s = input()
l = len(s)
s = list(s)
while True:
    flag = 0
    j = 0
    while j < len(s)-1:
        if s[j] == s[j+1]:
            s.pop(j)
            s.pop(j)
            flag = 1
        j += 1
    if flag == 0:
        break

if len(s) == 0: print('Empty String')
else: print(''.join(s))
=======
s = input()
l = len(s)
s = list(s)
while True:
    flag = 0
    j = 0
    while j < len(s)-1:
        if s[j] == s[j+1]:
            s.pop(j)
            s.pop(j)
            flag = 1
        j += 1
    if flag == 0:
        break

if len(s) == 0: print('Empty String')
else: print(''.join(s))
>>>>>>> d9a68cde1f68525c93033f7ea503a6293dfbd893
