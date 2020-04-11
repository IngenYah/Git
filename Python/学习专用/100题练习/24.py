#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
a = 2.0
b = 1.0
c = 0
amount = 0
for i in range(1,21):
    amount += a / b
    c = a
    a = a + b
    b = c
print(amount)