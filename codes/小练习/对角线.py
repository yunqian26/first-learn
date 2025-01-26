s=[]
sum=0
sum1=0
for i in range(3):
    s.append([])
    for j in range(3):
        s[i].append(int(input('输入一个数字： ')))
print(s[0])
print(s[1])
print(s[2])
for i in range(3):
    sum+=s[i][i]
    sum1+=s[i][2-i]
print('对角线之和为:',sum)
print('反对角线之和为:',sum1)