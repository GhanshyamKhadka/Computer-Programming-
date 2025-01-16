'''Write and test a function that determines if a given integer is a prime number. A
 prime number is an integer greater than 1 that cannot be produced by multiplying
 two other integers.'''

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print(is_prime(11))  
print(is_prime(15))  
print(is_prime(1))   
print(is_prime(17))  
