#输入某年某月某日，判断这一天是这一年的第几天？

y = int(input('year:'))
m = int(input('month:'))
d = int(input('day:'))
x = 0
leap = 28
month_big = 31
month_small = 30
if y % 400 == 0 or y % 4 == 0 and y % 100 != 0:
    leap = 29
if m > 2:
    x = 31 + leap
    for i in range(3,m):
        if i % 2 != 0:
            x += 31
        else:
            x += 30
elif m == 2:
    x = 31
x = x + d
print(x)