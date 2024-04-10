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

if __name__ == "__main__":

    menu = input("What would you like to do?\n1. Encode Passcode \n2. Decode Passcode\n:")
    passcode = input("Enter your passcode")
    encoded = encode(passcode)

    #testing testing 1 2 3
    print("This is a change") #change