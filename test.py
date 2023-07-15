import random
curr_num = 0
old_num = 0
i=0
while curr_num >= old_num:
    print("Level {} --> {}".format(i,curr_num))
    old_num = curr_num
    curr_num = random.randint(1,100000)
    i=i+1

print(" your score is {}".format(old_num))
print("You were defeated by number -> {}".format(curr_num))
