#include <iostream>
#include <string>
using namespace std;


string encrypt(const string& plaintext, int key) {
    string ciphertext = "";
    for (char c : plaintext) {
        if (isalpha(c)) { 
            char base = islower(c) ? 'a' : 'A';
            ciphertext += (c - base + key) % 26 + base; 
        } else {
            ciphertext += c; 
        }
    }
    return ciphertext;
}


string decrypt(const string& ciphertext, int key) {
    string plaintext = "";
    for (char c : ciphertext) {
        if (isalpha(c)) { 
            char base = islower(c) ? 'a' : 'A';
            plaintext += (c - base - key + 26) % 26 + base; 
        } else {
            plaintext += c; 
        }
    }
    return plaintext;
}

int main() {
    string text;
    int key, choice;

    cout << "Shift Cipher Program" << endl;
    cout << "1. Encrypt" << endl;
    cout << "2. Decrypt" << endl;
    cout << "Choose an option (1/2): ";
    cin >> choice;
    cin.ignore(); 

    cout << "Enter text: ";
    getline(cin, text);
    cout << "Enter key (shift amount): ";
    cin >> key;

    if (choice == 1) {
        string encryptedText = encrypt(text, key);
        cout << "Encrypted Text: " << encryptedText << endl;
    } else if (choice == 2) {
        string decryptedText = decrypt(text, key);
        cout << "Decrypted Text: " << decryptedText << endl;
    } else {
        cout << "Invalid option!" << endl;
    }

    return 0;
}
