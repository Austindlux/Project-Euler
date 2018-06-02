"""Project euler 28"""


total = 1
i = 3
side = 3
count = 0   

while i < 1002002:  # 1001 * 1001
    total += i
    count += 1

    if count == 4:  # This layer is finished 
        side += 2   # Add new layer
        count = 0

    i += side-1

print(total)