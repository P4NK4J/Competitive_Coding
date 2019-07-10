count = 0
for i in range(1, 2002):
    if (i % 3 == 0 or i % 4 == 0) and i % 5 != 0:
        count += 1

print(count)
