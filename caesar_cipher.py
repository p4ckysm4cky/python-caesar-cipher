encryptedText = []
def cipherInput():
    global plainText
    global key
    print("Welcome to the Caesar Cipher")
    plainText = input("Please enter the text you would like to encrypt\n:").lower()

    while True:
        key = input("Enter your key below\n:")
        if key.isnumeric() == True and int(key) <26 and int(key) >0:
            break
        else:
            print("---Please only enter numbers that are less than 26---")
    key = int(key)
    #for debugging
    #print("DEBUG-plainText:", plainText)
    #print("DEBUG-key:", key)


def cipherOutput():
    for i in plainText:
        if ord(i) > 96 and ord(i) < 123:
            ordinal = ord(i) + key
            if ordinal > 122:
                ordinal = ordinal - 26
        else:
            ordinal = ord(i)
        
        letter = chr(ordinal)
        #for debugging
        #print(chr(ord(i)), ord(i))
        #print(ord(letter))
        
        encryptedText.append(letter)
        #for debugging
        #print(encryptedText)

    print("Here is your encrypted message:\n---------------------------")    
    encryptNorm = ''.join(encryptedText)
    print(encryptNorm)



cipherInput()
cipherOutput()