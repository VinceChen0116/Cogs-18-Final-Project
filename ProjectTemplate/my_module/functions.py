
def decryption(message,code):  # My decryption function.
    decrypt_result=''       # Create a string that stores the decrypted result
    for item in message:    # loop thru all elements in input message
        if ord(item)>=65 and ord(item)<=90:   # check if the input element is A-Z, and if so, we will decrypt it.
            encrypt_upper=chr((ord(item)-65-code)%26+65)  # We calculate the shifted result by switching it to ASCII then back.
            decrypt_result=decrypt_result+encrypt_upper   # We add the bit to our created string.
        elif ord(item)>=97 and ord(item)<=122:  # check if the input element is a-z, and if so, we will decrypt it.
            encrypt_lower=chr((ord(item)-97-code)%26+97)  # We again calculate by switching it to ASCII and then switch back.
            decrypt_result=decrypt_result+encrypt_lower   # We add the bit to our created string.
        else:
            decrypt_result=decrypt_result+item   # If the input element is not A-Z or a-z, we will not switch it.
    return decrypt_result    # return our result.
""" Above is my drcryption function for my Caesar Function which takes two input, one is the message that will be decrypted, and the other is the shift code (How many bits the user wants the message to shift """

def encryption(message,code):  # My encryption function.
    encrypt_result=''      # Create a string that stores the encrypted result
    for item in message:   # loop thru all elements in input message
        if ord(item)>=65 and ord(item)<=90:   # check if the input element is A-Z, and if so, we will encrypt it.
            encrypt_upper=chr((ord(item)-65+code)%26+65)   # We calculate the shifted result by switching it to ASCII then back.
            encrypt_result=encrypt_result+encrypt_upper    # We add the bit to our created string.  
        elif ord(item)>=97 and ord(item)<=122:   # check if the input element is a-z, and if so, we will encrypt it.
            encrypt_lower=chr((ord(item)-97+code)%26+97)   # We again calculate by switching it to ASCII and then switch back.
            encrypt_result=encrypt_result+encrypt_lower    # We add the bit to our created string.
        else:
            encrypt_result=encrypt_result+item  # If the input element is not A-Z or a-z, we will not switch it.
    return encrypt_result  # return our result.
""" Above is my encryption function for my Caesar Function which takes two input, one is the message that will be encrypted, and the other is the shift code (How many bits the user wants the message to shift  """

def mainfunction(code,message,EDtype):  # Create our main function to output the correct result 
    if EDtype == 1:   # As the notebook file stated, if EDtype is 1, then it means that we will do ecnryption.
        return(encryption(message))  # Returned our encrypted result correctly.
    elif EDtype == 2:  # As the notebook file stated, if EDtype is 2, then it means that we will do decryption.
        return(decryption(message))  # Returned our decrypted result correctly.
    else:
        return('Please enter a valid Encryption and Decryption integer(1 or 2)')  # else return an error message.

""" Above is my main function to show the result for my Caesar Cipher function. It takes three inputs, which are the shift bit, the message that we will be encoding or decoding, and whether we want to do encryption or decryption."""
