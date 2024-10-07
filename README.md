# Caesar Cipher Tool

This is a Python program that implements the **Caesar Cipher** algorithm. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted by a certain number of positions down the alphabet.

## Features

- **Encrypt a message**: Shift each letter of the message by a specified number of positions in the alphabet.
- **Decrypt a message**: Revert the encrypted message back to its original form using the same shift value.
- Handles both uppercase and lowercase letters, as well as non-alphabet characters (which remain unchanged).
- User-friendly command-line interface for easy interaction.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Running the Program

1. Clone this repository to your local machine:

         git clone https://github.com/your-username/caesar-cipher-python.git

2.Navigate into the project directory:
  
        cd caesar-cipher-python

3.Run the caesar_cipher.py file:
  
        python caesar_cipher.py
  
## Example

    Encrypting a message:
        Input: Encrypt this message!
        Shift: 3
        Output: Hqfubsw wklv phvvdjh!

    Decrypting a message:
        Input: Hqfubsw wklv phvvdjh!
        Shift: 3
        Output: Encrypt this message!

## How it Works

Encryption: Each letter in the message is shifted forward by a number of positions defined by the shift value. If the shift passes the end of the alphabet, it wraps around to the beginning.
Decryption: The same process is applied in reverse, shifting letters backward to reveal the original message.

## Input Handling

Both uppercase and lowercase letters are supported.
Non-alphabet characters (spaces, punctuation, etc.) are not altered.

## License

This project is licensed under the MIT License. Feel free to use and modify it as you wish.
