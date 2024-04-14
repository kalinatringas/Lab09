# The password encoder should take in an 8-digit password in string format containing only integers.
# After passing the password into the encoder, the encoder stores the encoded password to a new
# variable, with each digit being shifted up by 3 numbers.
# Examples:
# “12345555” will become “45678888” after encoding.
# “00009962” will become “33332295” after encoding.

def encode(passC):
    passC = int(passC)
    encoded = []
    for i in range (len(passC)): 
        meow = passC[i] +3 
        encoded.append(meow)
    return encoded 

def decode (passC):
    #already should be an integer at this point
    decoded = []
    for i in range (len(passC)):
        meow = passC[i] - 3
        decoded.append(meow)
    return decoded 

if __name__ == "__main__":

    while menu != 3: 
        menu = input("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\nPlease enter an option: ")
        if menu == 1: 
            passcode = input("Please enter your password to encode: ")

            encoded = encode(passcode)
            print("Your password has been encoded and stored!")

        if menu == 2: 
            #put decoding function here
            print(f"The encoded password is X, and the original password is {passcode}")
        
