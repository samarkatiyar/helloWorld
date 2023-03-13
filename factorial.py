# Write a python module that can calculate the factorial of a number

# A factorial of a number is equal to

#  N * (N-1) * (N-2) ....... * 1    [until you reach 1] 


a = int(input("Hello! Welcome to FACTORIAL CALCULATOR. What number do you want to be cacuculated into its factorial? --> "))
print ("THIS IS THE ANSWER")

fact =1
i=1
for a in range(1,a+1):
    #print("I am processing the {}th loop with the value of a as {}".format(i,a))
    fact = fact * a
    i=i+1

print(fact)