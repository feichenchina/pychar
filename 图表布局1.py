#encoding:utf-8
# 作者：孙亚楠
# 日期：2020/3/21 0021 18:41
# 工具：PyCharm
# Python版本：3.7.3
#此python文件完成功能：
from pyecharts import Grid,Line,Bar
# //设置行名
columns = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
# //设置数据
data1 = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
data2 = [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]
# //设置折线图标题位置
line = Line("折线图","一年的降水量与蒸发量",title_top="45%")
line.add("降水量", columns, data1, is_label_show=True)
line.add("蒸发量", columns, data2, is_label_show=True)
grid = Grid()
# //设置柱状图的主标题与副标题
bar = Bar("柱状图", "一年的降水量与蒸发量")
# //添加柱状图的数据及配置项
bar.add("降水量", columns, data1, mark_line=["average"], mark_point=["max", "min"])
bar.add("蒸发量", columns, data2, mark_line=["average"], mark_point=["max", "min"])
# //设置两个图表的相对位置
grid.add(bar, grid_bottom="60%")
grid.add(line, grid_top="60%")
grid.render()