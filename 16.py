"""What is the sum of the digits of the number 2^1000?"""

product = str(2**1000)
sum_ = 0

for i in product:
    sum_ += int(i)

print(sum_)
