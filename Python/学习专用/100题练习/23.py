layer = int(input('输入层数：'))
if layer % 2 == 0:
    for l in range(1,(layer//2)+1):
        for i in range(1,layer-3-l):
            print(' ',end='')
        for i in range(1,l*2):
            print('*',end='')
        print(' ')
    for l in range(layer//2,0,-1):
        for i in range(1,layer-3-l):
            print(' ',end='')
        for i in range(1,l*2):
            print('*',end='')
        print(' ')
elif layer % 2 != 0:
    for l in range(1,((layer-1)//2)+1):
        for i in range(1,(layer-1)//2-l+2):
            print(' ',end='')
        for i in range(1,l*2):
            print('*',end='')
        print(' ')  
    for l in range(1,layer+1):
        print('*',end='')
    print(' ')
    for l in range((layer-1)//2,0,-1):
        for i in range(1,(layer-1)//2-l+2):
            print(' ',end='')
        for i in range(1,l*2):
            print('*',end='')
        print(' ')