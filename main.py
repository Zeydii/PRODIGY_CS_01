def caesar_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message


def caesar_decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted_message += chr(shifted)
        else:
            decrypted_message += char
    return decrypted_message


def main():
    choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()


    if choice == "encrypt":
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))
        encrypted = caesar_encrypt(message, shift)
        print("Encrypted message:", encrypted)
    elif choice == "decrypt":
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))
        decrypted = caesar_decrypt(message, shift)
        print("Decrypted message:", decrypted)
    else:
        print("Invalid choice. Please enter either 'encrypt' or 'decrypt'.")

main()



