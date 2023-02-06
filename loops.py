quest_and_ans = {
    "What is Samar's favorite color" : "red",
    "What is Samar's favorite food"  : "pizza",
    "What is Samar's favorite movie" : "Rise of Gru",
    "What is Samar's favorite subject" : "Math"
}

#print (quest_and_ans["What is Samar's favorite food"])
#print(quest_and_ans["What is Samar's favorite color"])
print ("Lets see if you really know Samar!!!!")
points = 0
for q in quest_and_ans:
    print(q)
    response = input("Guess the answer ==> ")
    if response.lower().replace(" ","") == quest_and_ans[q].lower().replace(" ",""):
        print("Bingo!!! You are correct")
        points = points + 1
    else:
        print("Ooh, Samar wont be happy that you dont know this")

print (" Thank you for playing. You scored %s points" % points)
#print(q + quest_and_ans[q])