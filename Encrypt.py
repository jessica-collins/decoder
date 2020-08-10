def encrypt(text,offset):
    """ Returns the entered text with the chosen coding offset

    Parameter:
    text (str): The text entered by user to be encrypted
    offset (int): The coding offset chosen by user
    """
    text=input("Please enter some text to encrypt:")
    offset=int(input("Please enter a shift onset (1-25):"))
    for i in text:
        text.index(i)
    return encrypted_text
