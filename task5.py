m = 0
for i in range(10000, 100000):
    if i % 133 == 125 and i % 134 == 111:
        m+=1
print(m)