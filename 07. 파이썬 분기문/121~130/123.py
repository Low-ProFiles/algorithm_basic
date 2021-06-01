#환율

n = list(input('입력: ').split())

if n[1] == '달러':
    print(int(n[0])*1167,'원')
elif n[1] == '엔':
    print(int(n[0])*1.096,'원')
elif n[1] == '유로':
    print(int(n[0])*1268,'원')
elif n[1] == '위안':
    print(int(n[0])*171,'원')

