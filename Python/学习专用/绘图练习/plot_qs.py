import matplotlib.pyplot as plt 

#定义x轴与y轴数据
x_data = ['2011','2012','2013','2014','2015']
y_data1 = [58000,60200,63000,71000,84000]
y_data2 = [10000,43000,12342,12400,80000]
#x_data代表横坐标值，y_data代表纵坐标值
ln1, = plt.plot(x_data,y_data1,color = 'red'  ,   linewidth = 1.5 , linestyle = ':')
ln2, = plt.plot(x_data,y_data2,color = 'yellow'   ,  linewidth = 1.5 , linestyle = '--')
#图例
plt.legend(handles=[ln2,ln1],labels=['Python','Java'],loc='best')
#调用show函数显示图像
plt.show()