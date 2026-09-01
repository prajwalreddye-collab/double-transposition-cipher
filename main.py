from encryption import encrypt
from decryption import decrypt

print("DOUBLE TRANSPOSITION CIPHER")
print("----------------------------")

text = input("Enter message: ")
key1 = int(input("Enter first key: "))
key2 = int(input("Enter second key: "))

encrypted = encrypt(text, key1, key2)

print("\nEncrypted text:", encrypted)

decrypted = decrypt(encrypted, key1, key2)

print("Decrypted text:", decrypted)