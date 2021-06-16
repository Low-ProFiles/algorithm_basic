def pickup_even(list):
    new = []
    for i in list:
        if i % 2 == 0:
            new.append(i)
    print(new)

pickup_even([3,4,5,6,7,8])