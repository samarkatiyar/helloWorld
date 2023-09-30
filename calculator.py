def calculator(a,b,c):
    a = float(a)
    c = float(c)

    if b == "+":
       return a + c
    elif b == '-':
        return a - c
    elif b == '*':
       return a * c
    elif b == '/':
       return a/c
    else:
       return False
    
a = float(input("ENTER THE FIRST NUMBER ==>"))
b = input("ENTER *,+,-,/ ==>") 
c = float(input("ENTER THE SECOND NUMBER ==>"))
print("Result of {} {} {} = {}".format(a,b,c,calculator(a,b,c)))
