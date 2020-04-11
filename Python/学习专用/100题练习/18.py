#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
a = int(input('输入a:'))
n = int(input('输入次数'))
s = 0
a_r = 0
a_rs = []
for i in range(1,n+1):
    for j in range(0,i):
        a_r += a * (10 ** j)
    s += a_r
    a_rs.append(a_r)
    a_r = 0
print(s,a_rs)