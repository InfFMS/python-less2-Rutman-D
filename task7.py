m = int(input())
l = 0
print(m)
for i in range(2, m):
    for j in range(2, i):
        if i % j == 0:
            l+=1
    if l == 0:
        print(i)
    l = 0
