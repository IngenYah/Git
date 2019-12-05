import matplotlib.pyplot as plt 
import matplotlib.font_manager as fm
my_font=fm.FontProperties(fname="C:\Windows\Fonts\simhei.ttf")
#定义x轴与y轴数据
x_data = ['2011','2012','2013','2014','2015']
y_data1 = [58000,60200,63000,71000,84000]
y_data2 = [10000,43000,52342,62400,80000]
#x_data代表横坐标值，y_data代表纵坐标值
ln1, = plt.plot(x_data,y_data1,color = 'red'  ,   linewidth = 1.5 , linestyle = ':',label='Python销售量')
ln2, = plt.plot(x_data,y_data2,color = 'yellow'   ,  linewidth = 1.5 , linestyle = '--',label='Java销售量')
#图例
plt.legend(loc='best')
plt.title('销售总量')
plt.xlabel('年份')
plt.ylabel('销售量')
#调用show函数显示图像
plt.show()