
def caesar_decrypt(text, shift):
    decrypted = ""

    for char in text:
        if char.isupper():
            decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            decrypted += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            decrypted += char

    return decrypted


message = input("Enter the encrypted message: ")
shift = int(input("Enter shift value: "))

result = caesar_decrypt(message, shift)

print("Decrypted message:", result)
