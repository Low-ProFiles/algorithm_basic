#대소문자 변환
number = list(input('주민등록번호: '))
cal1 = int(number[0])*2 + int(number[1])*3 + int(number[2])*4 + int(number[3])*5 + int(number[4])*6 + int(number[5])*7 + int(number[7])*8 + int(number[8])*9 + int(number[9])*2 + int(number[10])*3 + int(number[11])*4 + int(number[12])*5
cal2 = str(11 - (cal1 % 11))

if number[13] == cal2:
    print('유호한 주민등록번호입니다.')

else:
    print('유효하지 않은 주민등록번호입니다.')
    


