"""Find the sum of the digits in the number 100!"""

factorial = 1
total = 0

for i in range(1, 101):
    factorial *= i

print(factorial)
for c in str(factorial):
    total += int(c)

print(total)