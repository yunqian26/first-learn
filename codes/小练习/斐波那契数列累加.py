a=1
b=2#初始化
num=20#累加项数
sum=b/a#相加第一项
for i in range(a,num):#循环
    c=b
    b=a+b
    a=c
    sum+=b/a#相加通式
print(sum)