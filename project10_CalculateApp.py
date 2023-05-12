import art
import replit

print(art.logo)

def ope():
    loop=True
    while loop:
        global operation
        operation = input("Pick an operation: ")
        if not (operation == "+" or operation=="-" or operation=="*" or operation=="/"):
            print("Your operation is wrong. Please try again.")
        else:
            loop = False

def calculate(operation,number1,number2):
    if operation=="+":
        return number1+number2
    elif operation=="-":
        return number1-number2
    elif operation=="*":
        return number1*number2
    elif operation=="/":
        return number1/number2

def call():
    number1 = float(input("what is the first number? "))
    print("+\n-\n*\n/")
    conti=True
    while conti:
        ope()
        number2 = float(input("What's the next number? "))
        result = calculate(operation,number1,number2)
        print(f"{number1} {operation} {number2} = {result}")
        global choice
        choice = input(f"Type 'y' to continue calculating with {result}. Or type 'n' to start a new calculation. Or type 'end' to end the execution.")
        if choice =="n" :
            conti=False
        elif choice=="end":
            conti=False
            print("Thank you to use the calculator.")
        elif choice == "y":
            replit.clear()
            number1=result
        
restart=True
while restart:
    call()
    if choice =="y" or choice=="end":
        restart=False
