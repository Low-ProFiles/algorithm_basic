number = list(input('휴대전화 번호 입력: ').split('-'))

if number[0] == '011':
    print('당신은 SKT 사용자입니다.')
elif number[0] == '016':
    print('당신은 KT 사용자입니다.')
elif number[0] == '019':
    print('당신은 SKT 사용자입니다.')
elif number[0] == '010':
    print('당신은 알 수 없는 사용자입니다.')