a = int(input())
b = int(input())
c = int(input())
d = int(input())

if abs(a-c) == 2 and abs(b-d) == 1:
    print("Yes")
elif abs(a-c) == 1 and abs(b-d) == 2:
    print("Yes")
else:
    print("No")