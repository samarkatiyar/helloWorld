ans1=input("Welcome to Premium Division Cauculator or P.D.C. would you like me to teach your kids or help you cauculate a division question==>")
if ans1.lower().replace(" ","") == 'teach my kids division ' or 'teach my kids':
     print ("First Lesson, divide 2 digit numbers with 1 digit numbers ")
     print ("")
 
else:
    n=int(input("HELLO WELCOME TO DIVISION CAUCULATOR. ENTER THE FIRST NUMBER==>"))
    n2=int(input("ENTER THE SECOND NUMBER==>"))
    while n2 > n:
          n2 = int(input("PLEASE ENTER THE SECOND NUMBER AGAIN (it must be bigger than the first number)==>"))
          ans = n/n2
          print (" {} DIVIDED BY {} IS EQUAL TO {}".format(n,n2,ans))


