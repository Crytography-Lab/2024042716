# =============================================================================
# PROGRAM 1: Caesar Cipher – Message Encryption & Decryption
# =============================================================================
# Description:
#   The Caesar Cipher is one of the oldest and simplest substitution ciphers.
#   Each letter in the plaintext is shifted by a fixed number (the key) along
#   the alphabet. For decryption, the shift is reversed.
#
# Algorithm:
#   Encryption: C = (P + key) mod 26
#   Decryption: P = (C - key) mod 26
# =============================================================================

def caesar_encrypt(plaintext, key):
    """Encrypt the plaintext using Caesar Cipher with the given key."""
    ciphertext = ""
    for ch in plaintext.upper():
        if ch.isalpha():
            encrypted_char = chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += ch
    return ciphertext


def caesar_decrypt(ciphertext, key):
    """Decrypt the ciphertext using Caesar Cipher with the given key."""
    plaintext = ""
    for ch in ciphertext.upper():
        if ch.isalpha():
            decrypted_char = chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += ch
    return plaintext


def run_demo():
    """Run 4 sample input/output demonstrations."""

    test_cases = [
        ("HELLO WORLD",          3),
        ("CRYPTOGRAPHY",         7),
        ("ATTACK AT DAWN",      13),
        ("THE QUICK BROWN FOX", 17),
    ]

    print("=" * 60)
    print("         CAESAR CIPHER – Encryption & Decryption")
    print("=" * 60)

    for i, (message, key) in enumerate(test_cases, start=1):
        encrypted = caesar_encrypt(message, key)
        decrypted = caesar_decrypt(encrypted, key)
        match     = "OK" if decrypted == message.upper() else "FAIL"

        print(f"\n  --- Test Case {i} ---")
        print(f"  Plaintext  : {message}")
        print(f"  Key (shift): {key}")
        print(f"  Encrypted  : {encrypted}")
        print(f"  Decrypted  : {decrypted}")
        print(f"  Status     : [{match}]")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    run_demo()
