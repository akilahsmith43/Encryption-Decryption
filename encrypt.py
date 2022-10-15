encrypted_string = ""
decrypted_string = ""

while True:
    message = input("please input a message to be encrypted and decrypted \n")
    number = int(input("please input a number \n"))
    for i in message:
        encrypted_string += (chr(ord(i) + number))
    print(encrypted_string)
    for i in encrypted_string:
        decrypted_string += (chr(ord(i) - number))
    print(decrypted_string)
    more = input("Do you have more inputs (“y” or “n”) ? \n")
    if more not in "y":
        break
    
