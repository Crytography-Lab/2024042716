# =============================================================================
# PROGRAM 7: Double Columnar Transposition Cipher – Encryption & Decryption
# =============================================================================
# Description:
#   Applies columnar transposition twice using two separate keywords, providing
#   stronger security than a single transposition.
#
# Algorithm:
#   1. Pad plaintext with 'X' to fill grid of width = len(Key1).
#   2. Write row-by-row; read columns in alphabetical key order -> intermediate.
#   3. Apply columnar transposition again with Key2 -> final ciphertext.
#   Decryption reverses both transpositions in reverse order.
# =============================================================================

def get_column_order(key):
    """Return column indices sorted alphabetically by key letter."""
    indexed = sorted(enumerate(key.upper()), key=lambda x: (x[1], x[0]))
    return [i for i, _ in indexed]


def columnar_encrypt(text, key):
    """Single columnar transposition encryption."""
    key_len   = len(key)
    padded    = text.upper()
    remainder = len(padded) % key_len
    if remainder != 0:
        padded += 'X' * (key_len - remainder)
    num_rows  = len(padded) // key_len
    grid      = [list(padded[r * key_len:(r + 1) * key_len]) for r in range(num_rows)]
    order     = get_column_order(key)
    result    = ''.join(grid[row][col] for col in order for row in range(num_rows))
    return result, num_rows


def columnar_decrypt(ciphertext, key, num_rows):
    """Single columnar transposition decryption."""
    key_len = len(key)
    order   = get_column_order(key)
    cols    = {}
    idx     = 0
    for col in order:
        cols[col] = list(ciphertext[idx:idx + num_rows])
        idx += num_rows
    return ''.join(cols[c][r] for r in range(num_rows) for c in range(key_len))


def double_columnar_encrypt(plaintext, key1, key2):
    """Apply columnar transposition twice."""
    inter, rows1 = columnar_encrypt(plaintext, key1)
    cipher, rows2 = columnar_encrypt(inter,   key2)
    return cipher, rows1, rows2


def double_columnar_decrypt(ciphertext, key1, key2, rows1, rows2):
    """Reverse both transpositions."""
    inter     = columnar_decrypt(ciphertext, key2, rows2)
    plaintext = columnar_decrypt(inter,      key1, rows1)
    return plaintext.rstrip('X')


def run_demo():
    """Run 4 sample input/output demonstrations."""

    test_cases = [
        ("HELLOWORLD",    "SECRET",  "KEY"),
        ("CRYPTOGRAPHY",  "MATH",    "CRYPTO"),
        ("ATTACKATDAWN",  "ZERO",    "CODE"),
        ("NETWORKSECURITY","PYTHON", "LOCK"),
    ]

    print("=" * 68)
    print("  DOUBLE COLUMNAR TRANSPOSITION CIPHER – Encryption & Decryption")
    print("=" * 68)

    for i, (message, key1, key2) in enumerate(test_cases, start=1):
        encrypted, r1, r2 = double_columnar_encrypt(message, key1, key2)
        decrypted         = double_columnar_decrypt(encrypted, key1, key2, r1, r2)

        match = "OK" if decrypted == message.upper() else "FAIL"

        print(f"\n  --- Test Case {i} ---")
        print(f"  Plaintext  : {message.upper()}")
        print(f"  Key 1      : {key1.upper()}")
        print(f"  Key 2      : {key2.upper()}")
        print(f"  Encrypted  : {encrypted}")
        print(f"  Decrypted  : {decrypted}")
        print(f"  Status     : [{match}]")

    print("\n" + "=" * 68)


if __name__ == "__main__":
    run_demo()
