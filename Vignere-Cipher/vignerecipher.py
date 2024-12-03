import numpy as np

def generate_key(text, key):
    # Extend key agar sesuai dengan panjang teks.
    key = list(key)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(text, key):
    # Enkripsi menggunakan Vigenere Cipher.
    encrypted_text = []
    key = generate_key(text, key)
    for i in range(len(text)):
        if text[i].isalpha():
            shift = (ord(text[i].upper()) + ord(key[i].upper()) - 2 * ord('A')) % 26
            encrypted_char = chr(shift + ord('A')) if text[i].isupper() else chr(shift + ord('a'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(text[i])  
    return "".join(encrypted_text)

def decrypt_vigenere(ciphertext, key):
    # Dekripsi menggunakan Vigenere Cipher.
    decrypted_text = []
    key = generate_key(ciphertext, key)
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = (ord(ciphertext[i].upper()) - ord(key[i].upper()) + 26) % 26
            decrypted_char = chr(shift + ord('A')) if ciphertext[i].isupper() else chr(shift + ord('a'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(ciphertext[i]) 
    return "".join(decrypted_text)

if __name__ == "__main__":
    print("=== Vigenere Cipher ===")
    text = input("Masukkan teks (plaintext): ")
    key = input("Masukkan kunci (key): ")

    encrypted = encrypt_vigenere(text, key)
    print(f"Teks terenkripsi: {encrypted}")

    decrypted = decrypt_vigenere(encrypted, key)
    print(f"Teks setelah dekripsi: {decrypted}")
