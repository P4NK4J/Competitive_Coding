for i in range(int(input())):
    
    case = int(input())
    string = input()
    lis = []
    
    for j in string:
        if j == 'E': lis.append('S')
        else: lis.append('E')
    
    print('Case #'+str(i+1)+': '+''.join(lis))
