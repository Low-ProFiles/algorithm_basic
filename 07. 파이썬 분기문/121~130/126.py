#우편번호

n = list(input('우편번호: '))

if int(n[2]) >= 0 and int(n[2]) < 3:
    print('강북구')
elif int(n[2]) >= 3 and int(n[2]) < 6:
    print('도봉구')
elif int(n[2]) >= 6 and int(n[2]) < 10:
    print('노원구')
