def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test cases
print(is_prime(2))   
print(is_prime(3))
print(is_prime(4))   # f
print(is_prime(17))  
print(is_prime(25))  # f

# Determines if a number is prime