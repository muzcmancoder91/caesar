from helpers import alphabet_position, rotate_character                         

def encrypt(text, key):
    """Recieves text and a key word and encrypts the text using the key word as a cycling rotation amount."""
    new_text = ""                                                              
    sub_key = []
    non_alpha = 0
    for i in key:                                                               
        let = alphabet_position(i)
        sub_key.append(let)

    for index in range(len(text)):                                              
        if text[index].isalpha():                                            
          x = (index - non_alpha) % len(sub_key)
          new_char = rotate_character(text[index], sub_key[x])
          new_text = new_text + new_char
        else:                                                                   
            non_alpha = non_alpha + 1                                           
            new_text = new_text + text[index]                                   
    return new_text

def main():
    text = input("What message would you like to encrypt?  ")                   
    key = input("What keyword would you like the encryption set to?  ")         
    print(encrypt(text, key))                                                   

if __name__ == '__main__':
    main()