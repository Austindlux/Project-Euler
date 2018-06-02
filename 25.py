"""What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""

fibonacci_list = [1, 1]


while True:
    next_num = fibonacci_list[-1] + fibonacci_list[-2]  # Add last 2 numbers
    fibonacci_list.append(next_num)
    if len(str(next_num)) == 1000:  # Stop when the last number in the list has 1000 digits
            break

index = fibonacci_list.index(fibonacci_list[-1])
print(index+1)





