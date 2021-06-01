#점수 판별
grade = int(input('score: '))
if grade >= 81 and grade <= 100:
    print('grade is A')
elif grade >= 61 and grade <= 80:
    print('grade is B')
elif grade >= 41 and grade <= 60:
    print('grade is C')
elif grade >= 21 and grade <= 40:
    print('grade is D')
else:
    print('grade is E')