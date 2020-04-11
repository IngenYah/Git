#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
x = int(input('输入数字：'))
number = x
sign = 1
prime_factors = []
while sign == 1:
    for i in range(2,x+1):
        if x // i == 1:
            prime_factors.append(x)
            sign = 0
            break
        elif x % i == 0:
            prime_factors.append(i)
            x = x // i
            break
print(number,'有{}个质因数，他们分别是{}'.format(len(prime_factors),prime_factors))