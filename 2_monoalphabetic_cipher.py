# =============================================================================
# PROGRAM 2: Monoalphabetic Cipher – Message Encryption & Decryption
# =============================================================================
# Description:
#   The Monoalphabetic Cipher maps each plaintext letter to a unique ciphertext
#   letter using a fixed permutation of the 26-letter alphabet as the key.
#   Decryption uses the inverse substitution map.
#
# Algorithm:
#   1. Build encrypt map: plain[i] -> cipher[i] for i in 0..25
#   2. Build decrypt map: inverse of encrypt map
#   3. Substitute each letter through the respective map
# =============================================================================

PLAIN_ALPHABET  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CIPHER_ALPHABET = "QWERTYUIOPASDFGHJKLZXCVBNM"


def build_cipher_key(cipher_alphabet):
    """Build forward and inverse substitution maps."""
    ca = cipher_alphabet.upper()
    encrypt_map = {PLAIN_ALPHABET[i]: ca[i] for i in range(26)}
    decrypt_map = {ca[i]: PLAIN_ALPHABET[i] for i in range(26)}
    return encrypt_map, decrypt_map


def monoalphabetic_encrypt(plaintext, encrypt_map):
    """Encrypt plaintext using the monoalphabetic substitution map."""
    result = ""
    for ch in plaintext.upper():
        result += encrypt_map[ch] if ch.isalpha() else ch
    return result


def monoalphabetic_decrypt(ciphertext, decrypt_map):
    """Decrypt ciphertext using the inverse monoalphabetic substitution map."""
    result = ""
    for ch in ciphertext.upper():
        result += decrypt_map[ch] if ch.isalpha() else ch
    return result


def run_demo():
    """Run 4 sample input/output demonstrations."""

    encrypt_map, decrypt_map = build_cipher_key(CIPHER_ALPHABET)

    test_cases = [
        "HELLO",
        "CRYPTOGRAPHY",
        "NETWORK SECURITY",
        "THE QUICK BROWN FOX",
    ]

    print("=" * 62)
    print("      MONOALPHABETIC CIPHER – Encryption & Decryption")
    print("=" * 62)
    print(f"\n  Plain Alphabet : {PLAIN_ALPHABET}")
    print(f"  Cipher Alphabet: {CIPHER_ALPHABET}\n")

    for i, message in enumerate(test_cases, start=1):
        encrypted = monoalphabetic_encrypt(message, encrypt_map)
        decrypted = monoalphabetic_decrypt(encrypted, decrypt_map)
        match     = "OK" if decrypted == message.upper() else "FAIL"

        print(f"  --- Test Case {i} ---")
        print(f"  Plaintext  : {message}")
        print(f"  Encrypted  : {encrypted}")
        print(f"  Decrypted  : {decrypted}")
        print(f"  Status     : [{match}]\n")

    print("=" * 62)


if __name__ == "__main__":
    run_demo()
