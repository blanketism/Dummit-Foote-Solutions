def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm
    Returns (gcd, x, y) such that gcd = ax + by
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y


def main():
    a = int(input("Enter first integer a: "))
    b = int(input("Enter second integer b: "))
    
    gcd, x, y = extended_gcd(a, b)
    
    print(f"\nGCD({a}, {b}) = {gcd}")
    print(f"{gcd} = {a}*({x}) + {b}*({y})")
    
    # Verify the result
    result = a * x + b * y
    print(f"Verification: {a}*{x} + {b}*{y} = {result}")


if __name__ == "__main__":
    main()