import random

def game_round(bullseye):
    guessnum = int(input("Enter a number: "))
    numimportant = guessnum - bullseye
    if numimportant == 0:
        print("Yay! U got it right")
        return True
    elif numimportant in range(-20,-1):
        print("Your guess is a little less!")
    elif numimportant in  range(-100,-21):
        print("You're waaaay less!")
    elif numimportant in range(1,20):
        print('Your guess is a little big!')
    elif numimportant in range(21,40):
        print("Your guess is waaay too big!")
    elif numimportant in range(41,100):
        print("Your guess is super duper bigger!")
    return False

bullseye = random.randint(1,100)

for i in range(0,5):
    if game_round(bullseye):
        exit(0)

print("Nice Try, better luck next time. The number was {}".format(bullseye))

