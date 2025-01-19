def plus(n):
    if n==1 or n==0:
        sum=1
    else:
        sum=n*plus(n-1)
    return sum
print(plus(5))