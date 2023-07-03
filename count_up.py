i= int(input("enter a number===>"))
i3 = i
for i in range (-1,i-1):
    i2 = i3 - i
    i=i+1
    print ("It's {}  {} Left to go!".format(i,i2))
print ("It's {}".format(i))
