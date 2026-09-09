# =============================================================================
# PROGRAM 6: Rail Fence Cipher – Message Encryption & Decryption
# =============================================================================
# Description:
#   The Rail Fence Cipher writes plaintext in a zigzag pattern across n rails,
#   then reads each rail sequentially to produce the ciphertext.
#
# Algorithm:
#   Encryption: place characters on rails in zigzag order, read rail by rail.
#   Decryption: determine rail lengths, fill rails from ciphertext, re-read
#               characters in zigzag order.
# =============================================================================

def rail_fence_encrypt(plaintext, num_rails):
    """Encrypt plaintext using Rail Fence Cipher."""
    rails     = [[] for _ in range(num_rails)]
    rail      = 0
    direction = 1
    for ch in plaintext:
        rails[rail].append(ch)
        if rail == 0:
            direction = 1
        elif rail == num_rails - 1:
            direction = -1
        rail += direction
    return ''.join(''.join(r) for r in rails), rails


def rail_fence_decrypt(ciphertext, num_rails):
    """Decrypt ciphertext using Rail Fence Cipher."""
    n            = len(ciphertext)
    rail_pattern = []
    rail         = 0
    direction    = 1
    for _ in range(n):
        rail_pattern.append(rail)
        if rail == 0:
            direction = 1
        elif rail == num_rails - 1:
            direction = -1
        rail += direction

    rail_lengths  = [rail_pattern.count(r) for r in range(num_rails)]
    rail_contents = []
    idx = 0
    for length in rail_lengths:
        rail_contents.append(list(ciphertext[idx:idx + length]))
        idx += length

    rail_idx = [0] * num_rails
    result   = []
    for r in rail_pattern:
        result.append(rail_contents[r][rail_idx[r]])
        rail_idx[r] += 1
    return ''.join(result)


def run_demo():
    """Run 4 sample input/output demonstrations."""

    test_cases = [
        ("WEAREDISCOVERED",       3),
        ("HELLOWORLD",            2),
        ("CRYPTOGRAPHY",          4),
        ("THE QUICK BROWN FOX",   3),
    ]

    print("=" * 62)
    print("       RAIL FENCE CIPHER – Encryption & Decryption")
    print("=" * 62)

    for i, (message, rails) in enumerate(test_cases, start=1):
        encrypted, rail_contents = rail_fence_encrypt(message, rails)
        decrypted                = rail_fence_decrypt(encrypted, rails)
        match                    = "OK" if decrypted == message else "FAIL"

        print(f"\n  --- Test Case {i} ---")
        print(f"  Plaintext  : {message}")
        print(f"  Rails      : {rails}")
        for r, content in enumerate(rail_contents):
            print(f"  Rail {r}      : {''.join(content)}")
        print(f"  Encrypted  : {encrypted}")
        print(f"  Decrypted  : {decrypted}")
        print(f"  Status     : [{match}]")

    print("\n" + "=" * 62)


if __name__ == "__main__":
    run_demo()
