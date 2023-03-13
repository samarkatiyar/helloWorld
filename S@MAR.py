ans = int(input(" pick a 4 digit nmuber==>"))
confirm= input("IS {} THE 4 DIGIT NUMBER YOU WANT TO ENTER==>".format(ans))
points = 0
if confirm.lower().replace(" ","") == 'yes':
    print ("OKAY LET'S SEE WHAT HAPPENS NEXT")
    if ans == 1423:
      points = points + 10
      ans2 =  int(input(" BINGO!!! LET'S MOVE ON TO THE NEXT QUESTION! WHAT IS THE AREA OF A 125m BY 200m RECTANGLE(write the number only)==>"))
      if ans2 == 2500 :
         points = points + 10
         print ("YOU GOT {}/20".format(points))
          

      else: 
       print ("YOU GOT {}/20".format(points)) 
    else: 
      print ("YOU GOT {}/20".format(points))   
else:
     print("Okay come back soon!")  