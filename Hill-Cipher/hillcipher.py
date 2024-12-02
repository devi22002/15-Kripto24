import numpy as np

def enkripsi_hill(plain_text, matriks_kunci):
    n = len(matriks_kunci)
    plain_text = plain_text.replace(" ", "").upper()
    while len(plain_text) % n != 0:
        plain_text += "X"  # Padding dengan X jika panjang plaintext tidak sesuai

    # Konversi plaintext jadi matriks
    blok_plain = [
        [ord(huruf) - ord('A') for huruf in plain_text[i:i + n]]
        for i in range(0, len(plain_text), n)
    ]
    
    # Proses enkripsi
    cipher_text = ""
    for blok in blok_plain:
        hasil_kali = np.dot(matriks_kunci, blok) % 26
        cipher_text += "".join(chr(int(num) + ord('A')) for num in hasil_kali)

    return cipher_text

def mod_inverse(a, mod):
    # Cari invers modulo untuk dekripsi
    a = a % mod
    for x in range(1, mod):
        if ((a * x) % mod == 1):
            return x
    return None

def coprime(a, b):
    while b:
        a, b = b, a % b
    return a == 1

def dekripsi_hill(cipher_text, matriks_kunci):
    # Cari invers dari matriks kunci
    determinan = int(np.round(np.linalg.det(matriks_kunci)))
    if not coprime(determinan, 26):
        return "Error: Determinan matriks kunci tidak coprime dengan 26."
    
    determinan_inv = mod_inverse(determinan, 26)
    if determinan_inv is None:
        return "Error: Matriks kunci tidak valid untuk dekripsi."

    adjugate = np.round(determinan * np.linalg.inv(matriks_kunci)).astype(int) % 26
    matriks_kunci_inverse = (determinan_inv * adjugate) % 26
    
    # Konversi ciphertext jadi matriks
    n = len(matriks_kunci)
    blok_cipher = [
        [ord(huruf) - ord('A') for huruf in cipher_text[i:i + n]]
        for i in range(0, len(cipher_text), n)
    ]
    
    # Proses dekripsi
    plain_text = ""
    for blok in blok_cipher:
        hasil_kali = np.dot(matriks_kunci_inverse, blok) % 26
        plain_text += "".join(chr(int(num) + ord('A')) for num in hasil_kali)

    return plain_text

def cari_kunci(plain_text, cipher_text, ukuran_kunci):
    plain_text = plain_text.replace(" ", "").upper()
    cipher_text = cipher_text.replace(" ", "").upper()

    # Validasi panjang plaintext dan ciphertext
    if len(plain_text) != len(cipher_text):
        return "Error: Panjang plaintext dan ciphertext harus sama."

    # Buat matriks plaintext dan ciphertext
    blok_plain = [
        [ord(huruf) - ord('A') for huruf in plain_text[i:i + ukuran_kunci]]
        for i in range(0, len(plain_text), ukuran_kunci)
    ]
    blok_cipher = [
        [ord(huruf) - ord('A') for huruf in cipher_text[i:i + ukuran_kunci]]
        for i in range(0, len(cipher_text), ukuran_kunci)
    ]

    plain_matrix = np.array(blok_plain[:ukuran_kunci])
    cipher_matrix = np.array(blok_cipher[:ukuran_kunci])

    # Cari invers matriks plaintext
    determinan = int(np.round(np.linalg.det(plain_matrix)))
    if not coprime(determinan, 26):
        return "Error: Determinan matriks plaintext tidak coprime dengan 26."
    
    determinan_inv = mod_inverse(determinan, 26)
    if determinan_inv is None:
        return "Error: Matriks plaintext tidak memiliki invers modulo 26."

    adjugate = np.round(determinan * np.linalg.inv(plain_matrix)).astype(int) % 26
    plain_inverse = (determinan_inv * adjugate) % 26

    # Hitung matriks kunci
    matriks_kunci = (np.dot(cipher_matrix.T, plain_inverse)) % 26
    return matriks_kunci.astype(int)

def main():
    while True:
        print("\n=== Menu Hill Cipher ===")
        print("1. Enkripsi")
        print("2. Dekripsi")
        print("3. Cari Key")
        print("4. Exit")
        pilihan = input("Pilih opsi (1/2/3/4): ")
        
        if pilihan == "1":
            plain_text = input("Masukkan plaintext: ")
            ukuran_kunci = int(input("Masukkan ukuran matriks kunci (contoh: 2 untuk 2x2): "))
            print("Masukkan elemen matriks kunci:")
            matriks_kunci = []
            for _ in range(ukuran_kunci):
                baris = list(map(int, input().split()))
                matriks_kunci.append(baris)
            matriks_kunci = np.array(matriks_kunci)
            
            cipher_text = enkripsi_hill(plain_text, matriks_kunci)
            print(f"Hasil Enkripsi: {cipher_text}")
        
        elif pilihan == "2":
            cipher_text = input("Masukkan ciphertext: ")
            ukuran_kunci = int(input("Masukkan ukuran matriks kunci (contoh: 2 untuk 2x2): "))
            print("Masukkan elemen matriks kunci:")
            matriks_kunci = []
            for _ in range(ukuran_kunci):
                baris = list(map(int, input().split()))
                matriks_kunci.append(baris)
            matriks_kunci = np.array(matriks_kunci)
            
            plain_text = dekripsi_hill(cipher_text, matriks_kunci)
            print(f"Hasil Dekripsi: {plain_text}")

        elif pilihan == "3":
            plain_text = input("Masukkan plaintext: ")
            cipher_text = input("Masukkan ciphertext: ")
            ukuran_kunci = int(input("Masukkan ukuran matriks kunci (contoh: 2 untuk 2x2): "))
            
            matriks_kunci = cari_kunci(plain_text, cipher_text, ukuran_kunci)
            print("Matriks Kunci:")
            print(matriks_kunci)
        
        elif pilihan == "4":
            print("Program Selesai. Terima Kasih")
            break
        
        else:
            print("Input tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
