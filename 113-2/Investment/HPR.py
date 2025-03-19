from math import *




def p1_3f(f1, R, day):
    '''
    f1: final price
    R: rate
    '''
    return f1 - (f1 * R * (day / 365))

# holding period reburn
# p1 = f1
# Fourth Formula
def HPR(p0, p1, day):
    return (p1 - p0) / p0 * (365 / day)

# Test 01:
def test01():
    # ask price 
    p0 =  p1_3f(1000, 0.000127, 156)
    print(p0)

    # sell price
    p1 = p1_3f(1000, 0.00012, 156-56)
    print(p1)

    HPR_a = HPR(p1=p1, p0=p0, day=56)
    print(HPR_a)
    print(f"HPR: {round(HPR_a*100, 4)}%")
# 999.9457205479453
# 999.9671232876713
# 0.0001395075723944066

test01()
