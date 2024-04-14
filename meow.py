# The password encoder should take in an 8-digit password in string format containing only integers.
# After passing the password into the encoder, the encoder stores the encoded password to a new
# variable, with each digit being shifted up by 3 numbers.
# Examples:
# “12345555” will become “45678888” after encoding.
# “00009962” will become “33332295” after encoding.

def encode(passC):
    encoded = []
    for i in range (len(passC)): 
        meow = int(passC[i]) +3 #make it an integer so we can play with it 
        encoded.append(str(meow)) # make it back into a str
    return ''.join(encoded) 

def decode (passC):
    #already should be an integer at this point
    decoded = []
    for i in range (len(passC)):
        meow = int(passC[i]) - 3
        decoded.append(str(meow))
    return ''.join(decoded) 

if __name__ == "__main__":
    menu = "1"
    while menu: 
        menu = input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\nPlease enter an option: ")
        if menu == "1": 
            passcode = input("Please enter your password to encode: ")

            encoded = encode(passcode)
            print("Your password has been encoded and stored!")

        elif menu == "2": 
            #put decoding function here
            if 'encoded' in locals():
                decoded = decode(encoded)
                print(f"The encoded password is {encoded}, and the original password is {passcode}")
            else:
                print("You haven't encoded any password yet.")

        elif menu == "3":
            break

        else: 
            print("Invalid option. Please enter a valid option.")
        
