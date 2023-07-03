def square(x):
    return x*x

def power4(x,y):
    return square(square(x)) + square(square(y)) + 2*x*y * (2*square(x) + 2*square(y) + 3*x*y) 

a = float(input("Enter value of a ==>"))
b = float(input("Enter value of b ==>"))

print("Value of ({} + {})^4 is {}".format(a,b,power4(a,b)))

