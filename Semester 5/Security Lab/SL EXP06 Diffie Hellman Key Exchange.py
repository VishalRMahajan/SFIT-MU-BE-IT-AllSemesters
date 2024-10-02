def diffie_hellman_key_exchange(q, alpha, XA, XB):
    # Calculate the public keys
    YA = pow(alpha, XA, q)  # Alice's public key
    YB = pow(alpha, XB, q)  # Bob's public key
    
    # Calculate the shared secret keys
    shared_secret_Alice = pow(YB, XA, q)  # Alice calculates the shared key
    shared_secret_Bob = pow(YA, XB, q)    # Bob calculates the shared key
    
    return YA, YB, shared_secret_Alice, shared_secret_Bob

def main():
    print("Diffie-Hellman Key Exchange")
    
    # Input prime number q and base α
    q = int(input("Enter the prime number q: "))
    alpha = int(input("Enter the base α: "))
    
    # Input private keys XA and XB
    XA = int(input("Enter the private key of Alice XA: "))
    XB = int(input("Enter the private key of Bob XB: "))
    
    # Calculate the public keys and shared secret keys
    YA, YB, shared_secret_Alice, shared_secret_Bob = diffie_hellman_key_exchange(q, alpha, XA, XB)
    # Output the public keys and shared secret keys
    
    print("\nPublic Keys:")
    print(f"Alice's public key YA: {YA}")
    print(f"Bob's public key YB: {YB}")
    print("\nShared Secret Keys:")
    print(f"Alice's shared secret key: {shared_secret_Alice}")
    print(f"Bob's shared secret key: {shared_secret_Bob}")
    
    # Check if the shared secret keys match
    if shared_secret_Alice == shared_secret_Bob:
        print("The shared secret keys match. Key exchange successful!")
    else:
        print("The shared secret keys do not match. Key exchange failed.")

if __name__ == "__main__":
    main()
