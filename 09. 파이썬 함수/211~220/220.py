a, b, c = input().split()

def print_max():
    if a >= b:
        print(a)
    elif a >= c:
        print(a)
    elif b >= c:
        print(b)
    else:
        print(c)

print_max()