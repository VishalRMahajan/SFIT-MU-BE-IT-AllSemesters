def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find the greatest common divisor of a and b, and the coefficients of Bézout's identity."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(e, phi):
    """Calculate the modular inverse of e modulo phi using the Extended Euclidean Algorithm."""
    gcd, x, _ = extended_gcd(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist.")
    return x % phi

def rsa_key_generation(p, q, e):
    """Generate RSA public and private keys given primes p, q, and public exponent e."""
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("p and q must be prime numbers.")
    if not (1 < e < (p - 1) * (q - 1)):
        raise ValueError("e must be in the range 1 < e < (p-1)*(q-1)")

    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    
    return (e, n), (d, n)

def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def encrypt_decrypt(message, key, n):
    """Encrypt or decrypt a message using RSA."""
    e, d = key
    return pow(message, e, n) if e else pow(message, d, n)

def rsa_sign(message, private_key):
    """Generate a digital signature for a message using the private key."""
    d, n = private_key
    return encrypt_decrypt(message, (None, d), n)

def rsa_verify(message, signature, public_key):
    """Verify a digital signature for a message using the public key."""
    e, n = public_key
    message_prime = encrypt_decrypt(signature, (e, None), n)
    return message_prime == message

def main():
    # Key Generation
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))
    e = int(input("Enter public key exponent e: "))
    
    public_key, private_key = rsa_key_generation(p, q, e)
    print(f"Public Key: ({public_key[0]},  {public_key[1]})")
    print(f"Private Key: ( {private_key[0]},  {private_key[1]})")
    
    # Digital Signature Generation
    message = int(input("Enter a message (as an integer): "))
    signature = rsa_sign(message, private_key)
    print(f"Digital Signature: {signature}")

    # Signature Verification
    message_to_verify = int(input("Enter the message to verify (as an integer): "))
    signature_to_verify = int(input("Enter the digital signature to verify: "))
    
    if rsa_verify(message_to_verify, signature_to_verify, public_key):
        print("The message is authenticated, Accept")
    else:
        print("Message is altered, Discard!")

if __name__ == "__main__":
    main()
