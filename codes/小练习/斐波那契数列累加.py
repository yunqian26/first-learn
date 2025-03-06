count=0
for i in range(1000):
    if i % 5 != 0 and i % 6 != 0 and i % 8 != 0:
        count=count+1
print(count)