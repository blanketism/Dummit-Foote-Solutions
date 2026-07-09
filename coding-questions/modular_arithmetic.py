from euclidean_algorithm import extended_gcd

def mod_add(a, b, n):
    """Add two numbers modulo n without using %"""
    result = a + b
    while result >= n:
        result -= n
    return result


def mod_mult(a, b, n):
    """Multiply two numbers modulo n without using %"""
    result = 0
    a = a - (a // n) * n  # Reduce a mod n
    for _ in range(b):
        result += a
        while result >= n:
            result -= n
    return result

def mod_inverse(a, n):
    """
    If a and n are relatively prime, find c such that ac mod n = 1.
    Returns c if gcd(a,n) = 1, otherwise returns None.
    """
    gcd, x, _ = extended_gcd(a, n)
    if gcd != 1:
        return None
    # Reduce x to be in range [0, n)
    c = x - (x // n) * n
    if c < 0:
        c += n
    return c

if __name__ == "__main__":
    n = int(input("Enter modulus n: "))
    
    while True:
        print(f"\nModular arithmetic operations mod {n}:")
        print("1. Add two numbers")
        print("2. Multiply two numbers")
        print("3. Find modular inverse")
        print("4. Change modulus")
        print("5. Exit")
        
        choice = input("Choose an operation (1-5): ")
        
        if choice == "1":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(f"{a} + {b} mod {n} = {mod_add(a, b, n)}")
        elif choice == "2":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print(f"{a} * {b} mod {n} = {mod_mult(a, b, n)}")
        elif choice == "3":
            a = int(input("Enter number to find inverse for: "))
            inverse = mod_inverse(a, n)
            if inverse is not None:
                print(f"Modular inverse of {a} mod {n}: {inverse}")
                print(f"Verification: {a} * {inverse} mod {n} = {mod_mult(a, inverse, n)}")
            else:
                print(f"{a} and {n} are not relatively prime")
        elif choice == "4":
            n = int(input("Enter new modulus n: "))
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")