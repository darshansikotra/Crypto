# RAC implimentation in python

import rsa

public_key, private_key = rsa.newkeys(512)

message = input("Enter the message : ")

#Encrypt

ciphertext = rsa.encrypt(message.encode(), public_key)
print("Encrypted:", ciphertext)

#Decrypt
plaintext = rsa.decrypt(ciphertext,private_key)
print("Decrypted:", plaintext.decode())
