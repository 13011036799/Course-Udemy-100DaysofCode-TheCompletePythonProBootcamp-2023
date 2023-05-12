alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
    list = []
    text=text.lower()
    for i in range(len(text)):
        index = alphabet.index(text[i])
        index += shift
        e_letter = alphabet[index]
        list.append(e_letter)
    list = "".join(list)
    print(f"The encoded text is {list}")

def caesar(direction,text,shift):
    list = []
    text=text.lower()
    for i in range(len(text)):
        index = alphabet.index(text[i])
        if direction=="encode":
            index += shift
        elif direction=="decode":
            index -= shift
        else:
            attention=print("Your direction is wrong. Please answer the question again.")
            return attention
        letter = alphabet[index]
        list.append(letter)
    list = "".join(list)
    print(f"You choose {direction} operation. The decoded text is {list}.")
    
# another way
#def caesar(start_text, shift_amount, cipher_direction):
#    end_text = ""
#    if cipher_direction == "decode":
#        shift_amount *= -1
#        for letter in start_text:
#            position = alphabet.index(letter)
#            new_position = position + shift_amount
#            end_text += alphabet[new_position]
#            print(f"Here's the {direction}d result: {end_text}")

from art import logo
print(logo)

while loop:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26 # attention!!!
    caesar(direction,text,shift)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart=="no":
        loop=False
        print("Goodbye~")
# In this case, if the user enters a shift number greater than 26, the shift value will be adjusted to a value between 0 and 25, which is within the range of the alphabet indices. For example, if the user enters a shift value of 30, then shift % 26 will return 4, and the shift amount will be adjusted to 4.
