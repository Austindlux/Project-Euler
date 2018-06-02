"""Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""

def recurring_cycle(a, b):
    """Returns the length of the recurring cycle in a/b's decimal"""
    decimals = []
    remainder = []
    a *= 10

    while True:
        if a % b == a:
            a *= 10
            decimals.append(0)
            remainder.append('na') # Add this because we get length from remainder list, and 0 adds length
        else:
            c = a // b  # Decimal
            a = a % b   # Remainder
            if a in remainder:  # Getting a remainder we already got means its repeating
                length = len(remainder) - remainder.index(a) 
                return length
            if a == 0:  # No remainder the decimal does repeat
                return 0
            decimals.append(c)
            remainder.append(a)
            a *= 10

d = 0

for i in range(1, 1001):
    if recurring_cycle(1, i) > d:
        d = i

print(d)
