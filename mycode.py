N=int(input("HELLO. I AM 'IS IT DIVISIBLE BY THE NUMBER ROBOT'. OR I.I.D.B.T.N.R. what is the number.--> "))
N2=int(input("SECOND NUMBER-->"))
N3=N%N2
if N%N2 == 0:
    print("IT IS!!!")
else:
    print(" it is not!!!")
    print("THE REMANDER IS {}".format(N3))