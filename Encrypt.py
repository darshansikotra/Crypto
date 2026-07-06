#WAP to encrpt the string using seaser cipher.

def caesar_encrypt(text, shift):
    encrypted = ""

    for char in text:
        if char.isupper():
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65)

        elif char.islower():
            encrypted += chr((ord(char) - 97 + shift) % 26 + 97)

        else:
            encrypted += char

    return encrypted


message = input("Enter the message: ")
shift = int(input("Enter shift value: "))

result = caesar_encrypt(message, shift)

print("Encrypted message:", result)
