
p = int(input("Enter value of P: "))
g = int(input("Enter value of Generator: "))

alice_private = int(input("Enter private key of Alice: "))
bob_private = int(input("Enter private key of Bob: "))

print("\nAlice's Secret Private Key:", alice_private)
print("Bob's Secret Private Key:", bob_private)

alice_public = (g ** alice_private) % p
bob_public = (g ** bob_private) % p

print("\nAlice's Public Key sent to Bob:", alice_public)
print("Bob's Public Key sent to Alice:", bob_public)

# Shared secret calculation
alice_shared = (bob_public ** alice_private) % p
bob_shared = (alice_public ** bob_private) % p

print("\nAlice's calculated Shared Secret:", alice_shared)
print("Bob's calculated Shared Secret:", bob_shared)

if alice_shared == bob_shared:
    print("\nSuccess! Both parties have established the same shared secret key.")
else:
    print("\nError! Shared secrets do not match.")
