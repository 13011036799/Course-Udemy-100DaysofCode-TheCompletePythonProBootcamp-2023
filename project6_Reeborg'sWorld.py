# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# a robot in a Maze : find the flag
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if wall_on_right() and wall_in_front():
        turn_left()
    elif right_is_clear():
        turn_right()
        move()
    else:
        move()
     
#  Another way
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()        
    else:
        turn_left()
