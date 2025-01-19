def breaknum(num):
    if num < 10:
        return [num]
    else:
        return breaknum(num//10)+[num%10]

num=int(input('请输入一个数字： '))
break_num=breaknum(num)
print(break_num)
