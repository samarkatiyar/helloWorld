from decimal import Decimal
def series(n):
    if (2*n)%4 ==0:
        return -4/(2*n-1)
    else:
        return +4/(2*n-1)

def leibniz_pi():
    pi=Decimal(0)
    i=1
    while i < 10000000:
        pi = pi + series(Decimal(i))
        i=i+1
    print("Value of pi is --> {}".format(pi))

def pi():
    a = Decimal(1)
    ab = Decimal(3)
    pi= Decimal(0)
    i = 1
    while i < 100000000:
       c= 4/a -4/ab
       pi = pi + c
       a=a+4
       ab= ab+4
       i=i+1
    return pi
print(pi())
leibniz_pi()

    