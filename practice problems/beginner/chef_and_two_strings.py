t = int(input())
#lis = []
for i in range(t):
    s1 = input()
    s2 = input()
    l = len(s1)
    count1 = 0
    count2 = 0
    for j in range(l):
        flag = 0
        if s1[j] != s2[j]:
            count1 += 1
        if s1[j] == "?" and s2[j] == "?":
            count1 += 1
        if s1[j] != "?" and s2[j] != "?" and s1[j] != s2[j]:
            count2 += 1
        if s1[j] == s1[j] or s1[j] == "?" or s2[j] == "?":
            flag = 1
    print(count2,count1)
