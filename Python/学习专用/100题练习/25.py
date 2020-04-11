#求1+2!+3!+...+20!的和
amount = 0
a = 1
for i in range(1,21):
    for j in range(1,i+1):
        a = a * j
    amount += a
    a = 1
print(amount)

        