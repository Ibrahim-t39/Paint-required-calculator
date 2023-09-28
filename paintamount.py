import math
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
def paint_calc(height, width, cover):
    amount = math.ceil(((test_h * test_w) / coverage))
    print('You will need ' +  str(amount)  + ' cans of paint.')

paint_calc(height= test_h, width=test_w,cover=coverage)