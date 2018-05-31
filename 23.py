"""
A number n is called deficient if the sum of its proper divisors is less 
than n and it is called abundant if this sum exceeds n.
all integers greater than 28123 can be written as the sum of two abundant numbers
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

def is_abundant(n):
    """Returns True if the given number is abundant, False otherwise"""
    divisors = [1]
    for i in range(2, int(n**(.5))+1):
        if n % i == 0:
            if i*i == n:
                divisors.append(i)
                continue
            divisors.append(i)
            divisors.append(n/i)

    total = 0

    for divisor in divisors:
        total += divisor

    return total > n

# Stores all abundant numbers under 28111 in a list
abundant_nums = []
for i in range(12, 28112):
    if is_abundant(i):
        abundant_nums.append(i)

abundant_set = set(abundant_nums)

def is_abundant_sum(n):
    """Returns True if n can be written as the sum of two abundant numbers."""
    for i in abundant_nums:
        if n < i:
            return False
        if n-i in abundant_set:
            return True

total = 0
for i in range(1, 28124):
    if not is_abundant_sum(i):
        total += i

print(total)