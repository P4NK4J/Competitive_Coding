t = int(input())
while t > 0 :
    t -= 1
    n, m = [int(nun) for nun in input().split()]
    is_n_odd = (n % 2 == 1)
    is_m_odd = (m % 2 == 1)
    if is_m_odd and is_n_odd:
        print("NO")
    else:
        print("YES")
