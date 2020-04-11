#将一个列表的数据复制到另一个列表中。
l = int(input('你想输入的数字数量：'))
a = []
b = []
for i in range(0,l):
    print('请输入第',i+1,'个数字:',end='')
    a.append(int(input()))
b = a[:]
print(b)