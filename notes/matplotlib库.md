### matplotlib库
**基础绘图函数**
plt.plot()：用于绘制折线图、曲线图等。可以指定线条的颜色、线型、标记样式等参数，例如plt.plot(x, y, 'r--')表示绘制红色虚线。
plt.scatter()：用于绘制散点图。可以指定散点的大小、颜色、形状等参数，例如plt.scatter(x, y, s=50, c='blue', marker='o')表示绘制蓝色圆形散点。
plt.bar()：用于绘制柱状图。可以指定柱状图的宽度、颜色等参数，例如plt.bar(x, y, width=0.5, color='green')表示绘制绿色柱状图。
plt.hist()：用于绘制直方图。可以指定直方图的柱形数量、范围、是否累积等参数，例如plt.hist(data, bins=10, range=(0, 100), cumulative=True)表示绘制累积直方图。
plt.pie()：用于绘制饼图。可以指定饼图的突出显示、标签、颜色等参数，例如plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%')表示绘制带有百分比标签的饼图。
**图形设置函数**
plt.title()：设置图形的标题，例如plt.title('My Plot')。
plt.xlabel()和plt.ylabel()：分别设置x轴和y轴的标签，例如plt.xlabel('X Axis')和plt.ylabel('Y Axis')。
plt.xticks()和plt.yticks()：分别设置x轴和y轴的刻度，例如plt.xticks([0, 1, 2, 3])和plt.yticks([0, 50, 100])。
plt.xlim()和plt.ylim()：分别设置x轴和y轴的范围，例如plt.xlim(0, 10)和plt.ylim(0, 100)。
plt.grid()：设置是否显示网格，例如plt.grid(True)表示显示网格。
图形显示与保存函数
plt.show()：显示绘制的图形。
plt.savefig()：保存绘制的图形为文件，例如plt.savefig('my_plot.png')。
**子图相关函数**
plt.subplot()：创建子图，例如plt.subplot(2, 2, 1)表示创建一个2行2列的子图网格中的第1个子图。
plt.subplots()：创建多个子图并返回一个图形对象和子图轴对象的数组，例如fig, axs = plt.subplots(2, 2)。
其他常用函数
plt.text()：在图形上添加文本注释，例如plt.text(2, 3, 'Annotation')表示在坐标(2, 3)处添加文本注释。
plt.legend()：添加图例，例如plt.legend(['Line 1', 'Line 2'])表示添加图例。
plt.style.use()：设置图形的样式，例如plt.style.use('ggplot')表示使用ggplot样式。

##### 子库pyplot
* 用于绘制二维线图
* `matplotlib.pyplot([x], y, [fmt], *, data=None, **kwargs)`
* 参数说明：
x, y：点或线的节点，x 为 x 轴数据，y 为 y 轴数据，数据可以列表或数组。
fmt：可选，定义基本格式（如颜色、标记和线条样式）。
`**kwargs`：可选，用在二维平面图上，设置指定属性，如标签，线的宽度等。
颜色字符：'b' 蓝色，'m' 洋红色，'g' 绿色，'y' 黄色，'r' 红色，'k' 黑色，'w' 白色，'c' 青绿色，'#008000' RGB 颜色符串。多条曲线不指定颜色时，会自动选择不同颜色。
线型参数：'‐' 实线，'‐‐' 破折线，'‐.' 点划线，':' 虚线。
标记字符：'.' 点标记，',' 像素标记(极小点)，'o' 实心圈标记，'v' 倒三角标记，'^' 上三角标记，'>' 右三角标记，'<' 左三角标记...等等。
如果我们要绘制坐标 (1, 3) 到 (8, 10) 的线，我们就需要传递两个数组 [1, 8] 和 [3, 10] 给 plot 函数：

* 若未指定x轴，则会根据y轴数据分别设置(1,2,3,4......)
##### 绘图标记
* 给坐标定义一些不一样的标记可用plot()方法中的marker参数定义，参数如下：
|标记|描述|
|--|--|
|"."|点|
|","|像素点|
|"o"|实心圆|
|"v"|下三角|
|"^"|上三角|
|"<"|左三角|
|">"|右三角|
|"1"|下三叉|
|"2"|上三叉|
|"3"|左三叉|
|"4"|右三叉|
|"8"|八角形|
|"s"|正方形|
|"p"|五边形|
|"P"|加号（填充）|
|"`*`"|星号|
|"h"|六边形 1|
|"H"|六边形 2|
|"+"|加号|
|"x"|乘号 x|
|"X"|乘号 x (填充)|
|"D"|菱形|
|"d"|瘦菱形|
|"`|`"|竖线|
|"`_`"|横线|
|0 (TICKLEFT)|左横线|
|1 (TICKRIGHT)|右横线|
|2 (TICKUP)|上竖线|
|3 (TICKDOWN)|下竖线|
|4 (CARETLEFT)|左箭头|
|5 (CARETRIGHT)|右箭头|
|6 (CARETUP)|上箭头|
|7 (CARETDOWN)|下箭头|
|8 (CARETLEFTBASE)|左箭头 (中间点为基准)|
|9 (CARETRIGHTBASE)|右箭头 (中间点为基准)|
|10 (CARETUPBASE)|上箭头 (中间点为基准)|
|11 (CARETDOWNBASE)|下箭头 (中间点为基准)|
|"None", " " or ""|没有任何标记|
|'$...$'	|渲染指定的字符。例如 "$f$" 以字母 f 为标记|

* 运用该参数可定义节点的形状
* plot()方法中还有`fmt([marker][line][color])`参数用于设置线条样式和颜色
线类型：
|线类型标记|描述|
|--|--|
|'-'|实线|
|':'|虚线|
|'--'|破折线|
|'-.'|点划线| 

|颜色标记|描述|
|--|--|
|'r'|红色|
|'g'|绿色|
|'b'|蓝色|
|'c'|青色|
|'m'|品红|
|'y'|黄色|
|'k'|黑色|
|'w'|白色|


