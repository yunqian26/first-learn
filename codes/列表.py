candidate=['a','b','c','d','e','f','g','h']#定义一个列表
print('list:',candidate)#打印列表
candidate[4]='i'#修改列表
print('list:',candidate)#再次打印
candidate.insert(0,'z')#往列表头塞入元素
candidate.append('end')#往列表尾塞入元素
candidate.insert(5,'mid')#往列表中塞入元素
print('list:',candidate)#又打印一次列表
for i in range(2,len(candidate),1):#从第三项开始，循环次数等同于走到列表末
    print('MR'+candidate.pop(2)+' we are sorry to tell u')#将列表除了开头两个元素之外元素全部删除，并输出删除信息
print('list:',candidate)#打印
del candidate[0]#删除列表第一位元素
del candidate[0]#删除列表第二位元素
print('list:',candidate)#打印空列表