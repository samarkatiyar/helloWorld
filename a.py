#QUIZ
points = 0
q1 = input("WHAT IS THE CAPITAL OF INDIA. ENTER YOUR ANSWER HERE(please just write the answer. NOTHING ELSE!!)==>")
if q1.capitalize().replace(" ","") == 'NEW DELHI':
    print ("You got it correct!! You get a point!")
    print ("YOUR SCORE IS ==> {}".format(points))
else:
    print ("You got it wrong :(")
q2=input("What is the biggest country in the world. ENTER YOUR ANSWER HERE(please just write the answer. NOTHING ELSE!!)==>")
if q2.capitalize().replace(" ","") == 'RUSSIA':
    print ("You got it correct!! You get a point!")
    print ("YOUR SCORE IS ==> {}".format(points))
else:
    print ("You got it wrong :(")
q3=input("What is the lightest element. ENTER YOUR ANSWER HERE(please just write the answer. NOTHING ELSE!!)==>")
if q3.capitalize().replace(" ","") == 'HELIUM':
    print ("You got it correct!! You get a point!")
    print ("YOUR SCORE IS ==> {}".format(points))
else:
    print ("You got it wrong :(")