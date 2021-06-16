#새롭게 등장한 replace

def convert_int(num):
    return int(num.replace(',', ''))
    
print(convert_int("1,234,567"))