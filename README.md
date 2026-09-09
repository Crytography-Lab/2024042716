# Cryptography Lab Programs

**Student:** Jitin Kumar  
**Roll No:** 2024042716  
**Course:** Cryptography  

---

## Overview

This repository contains Python implementations of **7 classical cryptographic algorithms** as part of the Cryptography lab curriculum. Each program demonstrates both **encryption** and **decryption** with sample input/output.

---

## Programs

| # | Algorithm | File |
|---|-----------|------|
| 1 | **Caesar Cipher** | `1_caesar_cipher.py` |
| 2 | **Monoalphabetic Cipher** | `2_monoalphabetic_cipher.py` |
| 3 | **Polyalphabetic Cipher (Vigenère)** | `3_polyalphabetic_cipher.py` |
| 4 | **Hill Cipher** | `4_hill_cipher.py` |
| 5 | **Playfair Cipher** | `5_playfair_cipher.py` |
| 6 | **Rail Fence Cipher** | `6_rail_fence_cipher.py` |
| 7 | **Double Columnar Transposition Cipher** | `7_double_columnar_transposition.py` |

---

## How to Run

```bash
# Python 3.x required
python 1_caesar_cipher.py
python 2_monoalphabetic_cipher.py
python 3_polyalphabetic_cipher.py
python 4_hill_cipher.py
python 5_playfair_cipher.py
python 6_rail_fence_cipher.py
python 7_double_columnar_transposition.py
```

Each script is interactive — it will prompt you for the plaintext message and key, then display the encrypted and decrypted results.

---

## Algorithm Summaries

### 1. Caesar Cipher
Shifts each letter of the plaintext by a fixed number (the key) along the alphabet.
- **Encryption:** `C = (P + key) mod 26`
- **Decryption:** `P = (C - key + 26) mod 26`

### 2. Monoalphabetic Cipher
Maps each plaintext letter to a unique ciphertext letter using a fixed scrambled alphabet.
- **Key:** A permutation of all 26 letters (e.g., `QWERTYUIOPASDFGHJKLZXCVBNM`)
- Decryption uses the inverse substitution map.

### 3. Polyalphabetic Cipher (Vigenère)
Uses a repeating keyword to apply variable shifts to each letter.
- **Encryption:** `C[i] = (P[i] + K[i mod len(K)]) mod 26`
- **Decryption:** `P[i] = (C[i] - K[i mod len(K)] + 26) mod 26`

### 4. Hill Cipher
Encrypts blocks of letters using matrix multiplication modulo 26.
- **Key:** An invertible 2×2 matrix (determinant must be coprime with 26)
- **Encryption:** `C = K × P (mod 26)`
- **Decryption:** `P = K⁻¹ × C (mod 26)`

### 5. Playfair Cipher
Encrypts digraphs (pairs of letters) using a 5×5 key matrix. Rules:
- Same row → shift right
- Same column → shift down
- Rectangle → swap columns

### 6. Rail Fence Cipher
Writes plaintext in a zigzag across `n` rails, then reads off each rail in order.

### 7. Double Columnar Transposition Cipher
Applies columnar transposition twice using two separate keywords for enhanced security.

---

## Sample Output

```
===================================================
         CAESAR CIPHER – Encryption & Decryption
===================================================

  Original Plaintext  : HELLO WORLD
  Shift Key           : 3
  Encrypted Ciphertext: KHOOR ZRUOG
  Decrypted Plaintext : HELLO WORLD
  [OK] Decryption successful.
```

---

## Requirements

- Python 3.x (no external libraries required for the cipher programs)
