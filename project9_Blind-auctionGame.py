from replit import clear
from art import logo

def find_highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for name in bids:
        if highest_bid<bids[name]:
            highest_bid=bids[name]
            winner=name
    print(f"The winner is {name}. The price is {highest_bid}.")

print(logo+"\n")
loop=True
bids={}
while loop:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue=="no":
        loop = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
        
        
# art.py
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
