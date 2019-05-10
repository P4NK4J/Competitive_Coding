n = int(input())
s =  input()
k = int(input())
s = list(s)
for i in range(n):
    flag = 1
    c = 0
    d = 0
    k = k % 26
    if ord(s[i]) >= 97 and ord(s[i]) <= 122:
        c = ord(s[i]) + k
        if c > 122 :
            c = c - 26
        s[i] = chr(c)
    elif ord(s[i])>= 65 and ord(s[i]) <= 90:
         d = ord(s[i]) + k
         if d > 90 :
             d = d - 26
         s[i] = chr(d)
    else:
        flag = 0
s = "".join(s)
print(s)
    
