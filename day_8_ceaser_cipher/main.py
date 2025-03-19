ceaser_cipher_title = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88  
"""

alphabets = "abcdefghijklmnopqrstuvwxyz"

isStart = True


def encode(text, shift):
    encoded = ""
    for letter in text.lower():
        i = alphabets.index(letter)
        encoded += (alphabets[i + shift])
    return encoded


def decode(text, shift):
    decoded = ""
    for letter in text.lower():
        i = alphabets.index(letter)
        decoded += alphabets[abs(i - shift)]
    return decoded

print(ceaser_cipher_title)
while isStart:
    user_option = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ")
    shift = int(input("Type the shift number "))
    if user_option == "encode":
        encoded_text = encode(text, shift)
        print(f"Here is the encoded result: {encoded_text}")
    elif user_option == "decode":
        decoded_text = decode(text, shift)
        print(f"Here is the decoded result: {decoded_text}")
    else:
        print("Unknown input")
    toContinue = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if toContinue == "yes":
        isStart = True
    else:
        print("Goodbye! 🖐️")
        isStart = False
