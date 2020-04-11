f = [0 , 1]
for i in range(2,50):
    fi = f[i-1]+f[i-2]
    f.append(fi)
print(f)

x = int(input('输入你想知道的某个数字:'))
print(f[x-1])