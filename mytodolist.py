mytodolist = []

with open("todo.txt", 'r') as input_file:
    for line in input_file:
        print("Your to do list ==> " + line)
        mytodolist.append(line)

a = input("what do you want to add to your to do list? --->")
mytodolist.append(a)
print ("your thing has been added. thank you for choosing samar's list")
print (mytodolist)

with open("todo.txt","w") as output_file:
    for todo in mytodolist:
        output_file.write(todo)