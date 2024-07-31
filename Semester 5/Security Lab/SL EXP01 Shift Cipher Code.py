def plaintocipher(Plain, key):
    """
    Converts plaintext to ciphertext using the Caesar cipher method.

    Parameters:
    Plain (str): The plaintext message to be encrypted.
    key (int): The number of positions each letter in the plaintext is shifted.

    Returns:
    str: The encrypted ciphertext.
    """
    cipher = ""  # Initialize the ciphertext string
    for i in Plain:
        if i == " ":  # Preserve spaces as is
            cipher += " "
        elif i.isupper():  # Check if the character is uppercase
            # Convert the character using the key and add to the cipher string
            cipher += chr((ord(i) + key - 65) % 26 + 65)
        else:  # If the character is lowercase
            # Convert the character using the key and add to the cipher string
            cipher += chr((ord(i) + key - 97) % 26 + 97)
    return cipher  # Return the final ciphertext


def ciphertoplain(cipher, key):
    """
    Converts ciphertext back to plaintext using the Caesar cipher method.

    Parameters:
    cipher (str): The ciphertext message to be decrypted.
    key (int): The number of positions each letter in the ciphertext is shifted.

    Returns:
    str: The decrypted plaintext.
    """
    plain = ""  # Initialize the plaintext string
    for i in cipher:
        if i == " ":  # Preserve spaces as is
            plain += " "
        elif i.isupper():  # Check if the character is uppercase
            # Convert the character using the key and add to the plain string
            plain += chr((ord(i) - key - 65) % 26 + 65)
        else:  # If the character is lowercase
            # Convert the character using the key and add to the plain string
            plain += chr((ord(i) - key - 97) % 26 + 97)
    return plain  # Return the final plaintext


# Main program loop
while True:
    # Display the menu and get the user's choice
    choice = int(input("\n\nMenu \n1.PlainText to CipherText \n2.CipherText to PlainText \n3.BruteForce \n4.Exit\nEnter your Choice:"))

    if choice == 1:
        # Encrypt plaintext to ciphertext
        Plain = input("Enter the Plain Text: ")
        key = int(input("Enter the Key: "))
        print(Plain, "in cipher with", key, "is", plaintocipher(Plain, key))

    elif choice == 2:
        # Decrypt ciphertext to plaintext
        Cipher = input("Enter the Cipher Text: ")
        key = int(input("Enter the Key: "))
        print(Cipher, "in plain with", key, "is", ciphertoplain(Cipher, key))

    elif choice == 3:
        # Brute-force decryption
        cipher = input("Enter the Cipher Text: ")
        for i in range(26):  # Try all possible keys from 0 to 25
            brute = ""
            for j in cipher:
                if j == " ":  # Preserve spaces as is
                    brute += " "
                elif j.isupper():  # Check if the character is uppercase
                    # Convert the character using the key and add to the brute string
                    brute += chr((ord(j) - i - 65) % 26 + 65)
                else:  # If the character is lowercase
                    # Convert the character using the key and add to the brute string
                    brute += chr((ord(j) - i - 97) % 26 + 97)
            print("Key:", i, "->", brute)

    elif choice == 4:
        # Exit the program
        break

    else:
        # Handle invalid menu choices
        print("Enter a Valid Option")
