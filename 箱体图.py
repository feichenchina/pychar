#encoding:utf-8
# 作者：孙亚楠
# 日期：2020/3/21 0021 18:36
# 工具：PyCharm
# Python版本：3.7.3
#此python文件完成功能：
# //导入箱型图Boxplot
from pyecharts import Boxplot
boxplot = Boxplot("箱形图", "一年的降水量与蒸发量")
x_axis = ['降水量','蒸发量']
# //设置数据
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
y_axis = [data1,data2]
# //prepare_data方法可以将数据转为嵌套的 [min, Q1, median (or Q2), Q3, max]
yaxis = boxplot.prepare_data(y_axis)
boxplot.add("天气统计", x_axis, y_axis)
boxplot.render()