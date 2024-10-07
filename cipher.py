# Function to encrypt the message
def encrypt(text, shift):
    result = ""

    # Traverse through each character in the message
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # For non-alphabetic characters, just add them unchanged
        else:
            result += char
    return result

# Function to decrypt the message
def decrypt(text, shift):
    return encrypt(text, -shift)  # Decryption is just encryption with negative shift

# Main function to get user input and perform encryption/decryption
def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt or (Q)uit? ").lower()
        if choice == 'e':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'd':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose 'E', 'D', or 'Q'.")

if __name__ == "__main__":
    main()
