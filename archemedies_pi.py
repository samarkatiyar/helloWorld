import math
def get_circumference(n, s):
    s1_divide_by_2 = s/2
    a = math.sqrt(1 - s1_divide_by_2**2)
    b = 1 - a
    s2 = math.sqrt(b**2 + s1_divide_by_2**2)
    circumference = n * s
    diameter = 2
    return s2, circumference / diameter
n=6
s=1
for i in range(1,30):
    s, pi = get_circumference(n, s)
    n = n*2 
print("Value of Pi --> {}".format(pi))