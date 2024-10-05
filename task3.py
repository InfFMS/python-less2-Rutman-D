a = int(input())

if a % 10 == 2 or a % 10 == 3 or a % 10 == 4:
    print(a, "года")
elif a % 10 == 5 or a % 10 == 6 or a % 10 == 7 or a % 10 == 8 or a % 10 == 9 or a % 10 == 0:
    print(a, "лет")
elif a % 10 == 1:
    print(a, "год")


