"""Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""


def d(n):
    """Returns the sum of proper divisors of n"""
    divisors = []
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            divisors.append(i)

    total = 0
    for divisor in divisors:
        total += divisor

    return total

# Adds all amicable numbers between 1-10000 to the amicable_nums list
amicable_nums = []
for i in range(1, 10001):
    sum_i = d(i)
    sum_di = d(sum_i)
    if sum_di == i and sum_i != i and i not in amicable_nums:
        amicable_nums.append(sum_i)
        amicable_nums.append(i)

# Adds up all numbers in amicable_nums list
sum_of_nums = 0
for num in amicable_nums:
    sum_of_nums += num

print(sum_of_nums)