a = int(input())
b = int(input())
c = int(input())
d = int(input())

if abs(a-c) == abs(b-d):
    print("Yes")
elif abs(a-c) == 0 and abs(b-d) != 0:
    print("Yes")
elif abs(a-c) != 0 and abs(b-d) == 0:
    print("Yes")
elif abs(a-c) == 1 and abs(b-d) == 1:
    print("Yes")
else:
    print("No")