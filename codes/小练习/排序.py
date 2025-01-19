N=10
def selection(list):
    # 选择法排序
    for i in range(N - 1):
        min = i
        for j in range(i + 1, N):
            if list[min] > list[j]: min = j
        list[i], list[min] = list[min], list[i]

def bubble(list):
    for i in range(N - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                break
n=1
list=[]
for i in range(N):
    list.insert(0,int(input('输入第'+str(n)+'个数字： ')))
    n = n + 1
print('排列前：',end='')
print(list)
selection(list)
print('排列后：',end='')
print(list)
bubble(list)
print('排列后：',end='')
print(list)
