#제일 큰 수 출력

n1 = int(input('input number1: '))
n2 = int(input('input number2: '))
n3 = int(input('input number3: '))

if n1 >= n2 and n1 >= n3:
    print(n1)
elif n2 >= n1 and n2 >= n3:
    print(n2)
else:
    print(n3)