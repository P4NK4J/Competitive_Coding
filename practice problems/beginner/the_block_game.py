t = int(input())
for _ in range(t):
    s = input()
    sr = s[::-1]
    if sr == s:
        print("wins")
    else:
        print("losses")
