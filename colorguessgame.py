colors = ["RED","ORANGE","YELLOW","GREEN","BLUE","INDIGO","VIOLET"]
    
def game_round(computer_color):
    print(colors)
    user_color = ''
    while user_color not in colors:
        user_color = input("Please enter a color in the rainbow :==> ")
        user_color=user_color.upper()
    if user_color in colors:
        colors.remove(user_color)
    if user_color  == computer_color:
        return True
    else:
        return False  


def color_guessing_game():
    import random
    computer_color = colors[random.randint(0,6)]

    
    for i in range(0,5):
        if game_round(computer_color):
            print("Well done. Your score is {}".format(7-i))
            return
    
    print("Better luck next time")
    print("The answer was ==> {}".format(computer_color))
color_guessing_game()