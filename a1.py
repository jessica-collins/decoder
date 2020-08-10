#!/usr/bin/env python3
"""
Assignment 1
CSSE1001/7030
Semester 2, 2018
"""

from a1_support import is_word_english

__author__ = "Jessica Collins 44345956"

#ENCRYPTION FUNCTION
def encrypt(text,offset):
    """ Returns the entered text with the chosen coding offset

    Parameter:
    text (str): The text entered by user to be encrypted
    offset (int): The coding offset chosen by user

    Output:
    result (str): The text entered by the user, shifted by the chosen encryption offset
    """
    
    alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabet_caps='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    i=0
    letter=text[i]
    result = ''
    for letter in text:
        if ord(letter)==32:
            result=result+' '
        elif letter.isupper()==True:
            pos=alphabet_caps.index(letter)
            shift=pos+offset
            if shift>=26:
                result=result+alphabet_caps[shift-26]
            else:
                result=result+alphabet_caps[shift]
        elif letter.islower()==True:
            pos=alphabet.index(letter)
            shift=pos+offset
            if shift>=26:
                result=result+alphabet[shift-26]
            else:
                result=result+alphabet[shift]
        else:
            result=result+letter
       
    if offset==0:
        for n in range(1,26):
            encrypt(text,n)
    else:
        print (result)

#DECRYPTION FUNCTION
def decrypt(text,offset):
    """ Returns the entered text with the chosen coding offset

    Parameter:
    text (str): The text entered by user to be decrypted
    offset (int): The coding offset chosen by user

    Output:
    result (str): The text entered by the user, shifted by the chosen decryption offset
    """
    
    alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabet_caps='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    i=0
    letter=text[i]
    result = ''
    for letter in text:
        if ord(letter)==32:
            result+=' '
        elif letter.isupper()==True:
            pos=alphabet_caps.index(letter)
            shift=pos-offset
            if shift>=26:
                result=result+alphabet_caps[shift-26]
            else:
                result=result+alphabet_caps[shift]
        elif letter.islower()==True:
            pos=alphabet.index(letter)
            shift=pos-offset
            if shift>=26:
                result=result+alphabet[shift-26]
            else:
                result=result+alphabet[shift]
        else:
            result=result+letter

    if offset==0:
        for n in range(1,26):
            decrypt(text,n)
    else:
        print (result)

#AUTOMATIC DECRYPTION FUNCTION
def find_encryption_offsets(encrypted_text):
    """Returns the number of coding offsets possible for the entered encrypted text and returns the decrypted message if only 1 coding offset is found

    Parameters:
    encrypted_text (str): The encrypted message entered by the user

    Output:
    total (tuple): The possible offsets for the input text, where the offset is valid if the decrypted work is English
    english_word (str): The English word resulting from a single valid offset
    """

    alphabet='abcdefghijklmnopqrstuvwxyz'
    alphabet_caps='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    possible_offsets=()

    for offset in range(1,26):
        i=0
        letter=encrypted_text[i]
        result = ''
        english=()
        for letter in encrypted_text:
            if ord(letter)==32:
                result+=' '
            elif letter.isupper()==True:
                pos=alphabet_caps.index(letter)
                shift=pos-offset
                if shift>=26:
                    result=result+alphabet_caps[shift-26]
                else:
                    result=result+alphabet_caps[shift]
            elif letter.islower()==True:
                pos=alphabet.index(letter)
                shift=pos-offset
                if shift>=26:
                    result=result+alphabet[shift-26]
                else:
                    result=result+alphabet[shift]
            else:
                result=result+letter
        if is_word_english(result.lower())==True:
            possible_offsets+=(offset,)
            english_word=result
        else:
            possible_offsets+=()

    offset_list=list(possible_offsets)
    total=", ".join(map(str,offset_list))
    
    if len(possible_offsets)==1:
        print ('Encryption offset:', total, '\nDecrypted message:', english_word)
    elif len(possible_offsets)==0:
        print ('No valid encryption offset')
    else:
        print ('Multiple encryption offsets:', total)


def main():
    """Displays welcome message and option directory, will request input from user to determine which function is to be utilised

    Parameters:
    encrypted_text (str): The encrypted message entered by the user
    """
    print ("Welcome to the simple encryption tool!\n")
    response=input("Please choose an option [e/d/a/q]: \n  e) Encrypt some text \n  d) Decrypt some text \n  a) Automatically decrypt English text \n  q) Quit \n>")

    if response=='q':
        print (' Bye!')
    else:
        while response!='q':    
            if response=='e':
                text=input(" Please enter some text to encrypt:")
                offset=int(input(" Please enter a shift offset (1-25):"))
                encrypt(text,offset)
                response=input("\nPlease choose an option [e/d/a/q]: \n  e) Encrypt some text \n  d) Decrypt some text \n  a) Automatically decrypt English text \n  q) Quit \n>")
            elif response=='d':
                text=input(" Please enter some text to decrypt:")
                offset=int(input(" Please enter a shift offset (1-25):"))
                print (' The decrypted message is:')
                decrypt(text,offset)
                response=input("\nPlease choose an option [e/d/a/q]: \n  e) Encrypt some text \n  d) Decrypt some text \n  a) Automatically decrypt English text \n  q) Quit \n>")
            elif response=='a':
                encrypted_text=input(" Please enter some encrypted text:")
                find_encryption_offsets(encrypted_text)
                response=input("\nPlease choose an option [e/d/a/q]: \n  e) Encrypt some text \n  d) Decrypt some text \n  a) Automatically decrypt English text \n  q) Quit \n>")
            else:
                print (" Invalid command")
                response=input("\nPlease choose an option [e/d/a/q]: \n  e) Encrypt some text \n  d) Decrypt some text \n  a) Automatically decrypt English text \n  q) Quit \n>")
        print (' Bye!')
        pass


##################################################
# !! Do not change (or add to) the code below !! #
#
# This code will run the main function if you use
# Run -> Run Module  (F5)
# Because of this, a "stub" definition has been
# supplied for main above so that you won't get a
# NameError when you are writing and testing your
# other functions. When you are ready please
# change the definition of main above.
###################################################

if __name__ == '__main__':
    main()
