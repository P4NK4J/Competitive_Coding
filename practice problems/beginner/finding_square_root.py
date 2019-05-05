n = int(input())
lis1 = []
for i in range(n):
    lis = [int(x) for x in input().split()]
    for j in range(len(lis)):
        c = lis[j] ** (1/2)
        lis1.append(c)
for i in range(len(lis1)):
    print(int(lis1[i]))
