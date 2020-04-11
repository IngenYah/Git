#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
for x in range(2,1001):
    number = x
    factors = []
    reallynumber = 2
    for i in range(2,x):
        if x % i == 0:
            factors.append(i)
            factors.append(x // i)
    for factor in factors:
        reallynumber += factor
    if reallynumber // 2 == number:
        print(number,':',factors)