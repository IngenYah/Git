#判断101-200之间有多少个素数，并输出所有素数。
for i in range(101,201):
    x = 0
    for j in range(2,i):
        if i % j == 0:
            x = 1
    if x == 0:
        print(i,end=',')
print()


def prime():
    n = 2
    while 1:
        for i in range(2, n+1):
            if n%i:
                continue
            else:
                if i==n :
                    yield n
                else:
                    break
        n+=1
L = []
for i in prime():
    if 101<=i<=200:
        L.append(i)
    if i>=200:
        break
print('一共有{}个素数，这些素数分别是：{}'.format(len(L),L))