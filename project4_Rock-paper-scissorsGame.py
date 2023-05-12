rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

def choose(choice):
    global loop
    if int(choice) == 0:
        print(rock)
        loop = False
    elif int(choice) == 1:
        print(paper)
        loop = False
    elif int(choice) == 2:
        print(scissors)
        loop = False
    else:
        print("You give an invalid number. Please try again.")
    return loop
    
# you choose
loop = True
while loop:
    choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor. ")
    choice = int(choice)
    choose(choice)

# the computer choose
computer = random.randint(0,3)
# print(type(computer))
print("\nThe computer choose: ")
choose(computer)

# get the result
if (choice == 0 and computer==1) or (choice == 1 and computer==2) or (choice == 2 and computer==0):
    print("You lose.")
elif (choice == 1 and computer==0) or (choice == 2 and computer==1) or (choice == 0 and computer==2):
    print("You win.")
else:
    print("You and the computer draw.")
