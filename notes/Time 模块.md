### Time 模块
* 通过`import time`来导入time模块
以下为常用函数
>`time.sleep()`暂停执行指令的秒数
>`time.localtime()`返回值为本地时间
>`time.gmtime()`返回值为UTC时间
>`time.strftime(转化后格式,时间)`将时间格式转化为字符串
>`time.strptime(字符串,转化后格式)`将字符串转化为时间格式
>`time.process_time()`程序运行时间

* 常用的格式代码 ：<br>%Y：四位数年份（例如2024）<br>%m：两位数月份（例如01，02）<br>%d：一个月中第几天（01到31）<br>%H：两位数的小时（00到23）<br>%M：两位数的分钟（00到59）<br>%S：两位数的秒（00到59）<br>%A：星期几的全称（Monday到Sunday）<br>%B：月份的全称（January到December）