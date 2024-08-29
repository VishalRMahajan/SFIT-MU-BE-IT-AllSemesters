def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find the greatest common divisor and coefficients."""
    if a == 0:
        return (b, 0, 1)
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return (g, x, y)

def calculate_d(e, phi):
    """Calculate private key d using Extended Euclidean Algorithm."""
    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise ValueError(f"e and phi must be coprime, but gcd(e, phi) = {g}")
    return x % phi

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_keys(p, q, e):
    """Generate RSA public and private keypair given primes p, q, and public exponent e."""
    # Compute modulus
    n = p * q
   
    # Compute totient function
    phi = (p - 1) * (q - 1)
   
    # Compute private exponent d
    d = calculate_d(e, phi)
   
    return ((e, n), (d, n))  # public_key, private_key

def encrypt(public_key, plaintext_int):
    """Encrypt an integer plaintext using the public key."""
    e, n = public_key
    # Encrypt the plaintext integer
    ciphertext_int = pow(plaintext_int, e, n)
    return ciphertext_int

def decrypt(private_key, ciphertext_int):
    """Decrypt a ciphertext integer using the private key."""
    d, n = private_key
    # Decrypt the ciphertext integer
    plaintext_int = pow(ciphertext_int, d, n)
    return plaintext_int

def main():
    while True:
        print("RSA Key Generation and Communication")
       
        # Party A key generation
        print("\nParty A Key Generation")
        p_a = int(input("Enter prime number p for Party A: "))
        q_a = int(input("Enter prime number q for Party A: "))
        e_a = int(input("Enter public key exponent e for Party A: "))
       
        if not (is_prime(p_a) and is_prime(q_a)):
            print("Both p and q must be prime numbers.")
            continue
       
        public_key_a, private_key_a = generate_keys(p_a, q_a, e_a)
        print(f"\nParty A Public Key: (e = {public_key_a[0]}, n = {public_key_a[1]})")
        print(f"Party A Private Key: (d = {private_key_a[0]}, n = {private_key_a[1]})")

        # Party B key generation
        print("\nParty B Key Generation")
        p_b = int(input("Enter prime number p for Party B: "))
        q_b = int(input("Enter prime number q for Party B: "))
        e_b = int(input("Enter public key exponent e for Party B: "))
       
        if not (is_prime(p_b) and is_prime(q_b)):
            print("Both p and q must be prime numbers.")
            continue
       
        public_key_b, private_key_b = generate_keys(p_b, q_b, e_b)
        print(f"\nParty B Public Key: (e = {public_key_b[0]}, n = {public_key_b[1]})")
        print(f"Party B Private Key: (d = {private_key_b[0]}, n = {private_key_b[1]})")

        # Encryption by Party A for Party B
        plaintext_int = int(input("\nParty A: Enter the integer message to encrypt: "))
        ciphertext_a = encrypt(public_key_b, plaintext_int)
        print(f"Party A encrypted message (ciphertext): {ciphertext_a}")

        # Decryption by Party B
        decrypted_message_b = decrypt(private_key_b, ciphertext_a)
        print(f"Party B decrypted message: {decrypted_message_b}")

        # Encryption by Party B for Party A
        plaintext_int_b = int(input("\nParty B: Enter the integer message to encrypt: "))
        ciphertext_b = encrypt(public_key_a, plaintext_int_b)
        print(f"Party B encrypted message (ciphertext): {ciphertext_b}")

        # Decryption by Party A
        decrypted_message_a = decrypt(private_key_a, ciphertext_b)
        print(f"Party A decrypted message: {decrypted_message_a}")

        # Continue or exit
        cont = input("\nDo you want to perform another operation? (yes/no): ")
        if cont.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
