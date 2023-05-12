print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choose1 = input("You come to a forest.Now you have two choices.Turn left or turn right? Which one do you choose? (left or right) ")
if choose1=="left":
    choose2 = input("Now you came to an ocean. Now you have two choices.Swim or wait? Which one do you choose? (swim or wait) ")
    if choose2 =="wait":
        choose3 = input("An angle bring you to a house. The house has 3 doors and they have different colors. Now you can choose one door to open. Which one will you choose? (red, blue or yellow) ")
        if choose3 =="red":
            print("You are burned by fire with the house. Game over.")
        elif choose3 =="blue":
            print("You are eaten by beats in the house. Game over.")
        elif choose3 =="yellow":
            print("You find the treasure in the house. You win!")
        else:
            print("You give up to go into the house and back to your house. Game over.")
    else:
        print("Sorry, you are attacked by trout. Game over.")
else:
    print("Sorry, you fall into a hole. Game over.")
