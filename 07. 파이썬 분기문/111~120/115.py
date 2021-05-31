a = int(input())
b = a - 20

if b < 0:
    print(0)
elif b >= 0 and b <= 255:
    print(b)
else:
    print(255)