def print_5xn(sentence):
    temp = int(len(sentence)/5)
    for x in range(temp+1):
        print(sentence[x * 5: x * 5 + 5])

print_5xn("아이엠어보이유알어걸앤유?")
