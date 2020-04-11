#a_money = int(input('当月销售额：(万元)'))     #int(input())输入的成为int，不然则是str
#if (a_money <= 10):
#    print('利润',a_money*0.1)
#elif (10 < a_money <= 20):
#    print('利润',1 + (a_money - 10)*0.05)

i = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*(rat[idx])
        i=arr[idx]
print (r)