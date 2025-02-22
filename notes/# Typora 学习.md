# Typora 学习  
### 标题语法:<br>
>使用井号键（#）设置标题，井号越多标题等级越低，字号越小，**井号后记得空格**  

### 段落语法  
>用**空白行**将一行或多行文本分隔，形成段落  

### 换行段落  
>用两个/一个空格/`<br>`换行  

### 强调语法  
>用`*`或`_`号作为强调标志  
>在目标两端各自加上一个符号为斜体 eg: *Typora*  
>加上两个符号为强调 eg: **Typora**  
>加上三个符号为斜体＋强调 eg: ***Typora***  

### 引用语法
>在语句前加上`>`符号,符号数量越多嵌套等级越低
>一级
>
>> 二级
>> > 三级
>> > 等级最高为十级
>> >
>> > >>>>>>> ovo

### 列表语法
>在语句前加上`-`/`+`/`*`符号
+ 1
+ 2
	another line
+ 3
**连续使用时需使用相同符号**,否则间距会偏大  
需要在保留连续性插入另一种元素,换行缩进一个制表符后输入
- 12
+ 3
* 54

### 代码语法
>将目标语句表示为代码,用一组 ` 号包括
>若目标语句中含有反引号则使用一组``包括
>制作代码块则将每一行缩进至少一个制表符
	#include<stdio.h>
	int main()
	{
	printf("hello world!\n");
	}
>本质作用:代码块/代码中的一切markdown语法不生效

### 分隔线
>使用两个空白行与一行`***`制作分隔线

***

### 链接语法:
>基本:格式:`[超链接显示名](超链接地址)`
>以下是几种基本格式(切换到源代码模式)
>可使用加粗/斜体
**[这是一个网站](https://www.bilibili.com/)**
<https://www.bilibili.com/>
https://markdown.com.cn/basic-syntax/links.html

引用链接格式:
`[数字]:网址 (标题)
[1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)
[1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> "Hobbit lifestyles"

### 图片语法
>`![图片名字](图片地址)`
>给图片添加链接如下:  
>`[![图片名字](图片地址)](图片链接)]