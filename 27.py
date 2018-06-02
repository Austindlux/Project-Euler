"""
n2+an+b, where |a|<1000 and |b|≤1000, n is the absolute value
ind the product of the coefficients, a and b, for the quadratic 
expression that produces the maximum number of primes for consecutive values of n, starting with n=0."""

def is_prime(num):
    """Returns True if the number is prime."""
    for i in range(2, int(num**(.5))+1):
        if num % i == 0:
            return False
    return True

def number_of_primes(a, b):
    """Returns the number of primes for consecutive values of n the equation has, given a and b"""
    n = 0
    while True:
        num = abs(n**2 + (a*n) + b)
        if not is_prime(num):
            return n-1
        n += 1

equation = [0] # Stores the number of primes, along with a and b of equation that has most primes

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        prime_nums = number_of_primes(a, b)
        if prime_nums > equation[0]:
            equation = [prime_nums, a, b]

print(equation[1] * equation[2])