for i in range(1, 10):#外循环，用于制作列的数量
    if i!=1:print()#用于每次循环一行后换行，另让第一行不空
    for j in range(1, i+1):#内循环，用于制作行的数量
        print (str(i)+'*'+str(j)+'='+str(i*j), end=' ')#打印并让print函数不默认换行