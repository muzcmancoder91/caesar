from sys import argv, exit
from helpers import alphabet_position, rotate_character                         

def encrypt(text, rot):
    """Receives text and a rotation number, and returns an encrypted message."""
    encrypt_text = ""
    for char in text:
        letter = rotate_character(char, rot)                                    
        encrypt_text = encrypt_text + letter                                    
    return encrypt_text

def user_input_is_valid(cl_args):
    #return len(argv) == 2 and argv[-1].isdigit()                               
    return len(cl_args) == 2 and cl_args[1].isdigit()       

def main():
    if user_input_is_valid(argv) == True:
        pass
    else:
        print("Please only rotate by a whole number, typed after the program name. (ex: caesar.py 5)")
        exit()

    text = input("What message would you like to encrypt?  ")                   
    rot = int(argv[1])                                                          

    #print(user_input_is_valid(argv[-1]))
    print(encrypt(text, rot))                                                   

if __name__ == '__main__':
    main()