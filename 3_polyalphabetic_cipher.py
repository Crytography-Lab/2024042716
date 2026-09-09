# =============================================================================
# PROGRAM 3: Polyalphabetic Cipher (Vigenere) – Encryption & Decryption
# =============================================================================
# Description:
#   The Vigenere Cipher uses a repeating keyword to shift each letter of the
#   plaintext by a variable amount, making frequency analysis harder.
#
# Algorithm:
#   Encryption: C[i] = (P[i] + K[i mod len(K)]) mod 26
#   Decryption: P[i] = (C[i] - K[i mod len(K)] + 26) mod 26
# =============================================================================

def vigenere_encrypt(plaintext, key):
    """Encrypt plaintext using the Vigenere cipher."""
    key       = key.upper()
    result    = ""
    key_index = 0
    for ch in plaintext.upper():
        if ch.isalpha():
            shift  = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            result += ch
    return result


def vigenere_decrypt(ciphertext, key):
    """Decrypt ciphertext using the Vigenere cipher."""
    key       = key.upper()
    result    = ""
    key_index = 0
    for ch in ciphertext.upper():
        if ch.isalpha():
            shift  = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(ch) - ord('A') - shift + 26) % 26 + ord('A'))
            key_index += 1
        else:
            result += ch
    return result


def run_demo():
    """Run 4 sample input/output demonstrations."""

    test_cases = [
        ("HELLOWORLD",           "KEY"),
        ("CRYPTOGRAPHY",         "SECRET"),
        ("ATTACK AT DAWN",       "LEMON"),
        ("THE QUICK BROWN FOX",  "CIPHER"),
    ]

    print("=" * 65)
    print("  POLYALPHABETIC (VIGENERE) CIPHER – Encryption & Decryption")
    print("=" * 65)

    for i, (message, key) in enumerate(test_cases, start=1):
        encrypted = vigenere_encrypt(message, key)
        decrypted = vigenere_decrypt(encrypted, key)
        match     = "OK" if decrypted == message.upper() else "FAIL"

        print(f"\n  --- Test Case {i} ---")
        print(f"  Plaintext  : {message}")
        print(f"  Keyword    : {key}")
        print(f"  Encrypted  : {encrypted}")
        print(f"  Decrypted  : {decrypted}")
        print(f"  Status     : [{match}]")

    print("\n" + "=" * 65)


if __name__ == "__main__":
    run_demo()
