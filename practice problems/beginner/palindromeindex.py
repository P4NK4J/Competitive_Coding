n = int(input())
lis = []
for i in range(n):
    s = input()
    rev = "".join(reversed(s))
    if rev == s:
        print("-1")
    else:
        for i in range(len(s)//2):
            if s[i] != s[len(s)- 1 -i]:
                temp = list(s)
                temp.pop(len(temp)-1-i)
                rev = "".join(reversed(temp))
                temp = "".join(temp)
                if rev == temp:
                    print(len(s) -1 -i)
                    break
                else:
                    print(i)
                    break
            
