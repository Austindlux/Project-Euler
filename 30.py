"""Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""

def sum_of_fifth_powers(num):
    """Returns True if num is the sum of fifth powers of it's digits"""
    digits = str(num)
    total = 0
    for i in digits:
        total += int(i)**5

    if total == num:
        return True

    return False

total = 0

for i in range(2, 295245):   # 295245 is 9^5 * 5
    if sum_of_fifth_powers(i):
        total += i

print(total)