def printmxn(sentence, num):
    temp = int(len(sentence)/num)
    for i in range(temp + 1):
        print(sentence[i*num: i*num+num])

printmxn("아이엠어보이유알어걸", 3)
