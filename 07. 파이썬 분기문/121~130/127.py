n = list(input('주민등록번호: '))

if int(n[7]) == 1 or int(n[7]) == 3:
    print('남자')
elif int(n[7]) == 2 or int(n[7]) == 4:
    print('여자')
