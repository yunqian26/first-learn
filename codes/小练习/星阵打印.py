lines=7
for i in range(1,lines,2):
    space=' '*((lines-i)//2)
    star='*'*i
    print(space+star+space)
for i in range(lines,0,-2):
    space = ' ' * ((lines - i) // 2)
    star = '*' * i
    print(space + star + space)