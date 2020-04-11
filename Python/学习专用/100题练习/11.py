#古典问题：有一个兔子，从出生后第3个月起每个月都生一个兔子，小兔子长到第三个月后每个月又生一个兔子，假如兔子都不死，问每个月的兔子总数为多少？
rs = [1,0]
r_n = []
x = int(input('输入你想知道的月份：'))
x = x - 1
now = 0
if x > 2:
    for i in range(2,x+1):
        new = 0
        for r in rs:
            new += r
        new = new  - rs[i-1]
        rs.append(new)
else:
    new = 0
print(rs)
for r in rs:
    now += r
    r_n.append(now)
print(r_n)

