
ones = ["one", "two", "three", "four", "five", "six", "seven", 
        "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]

answer = 0


def add_letters(number):
    """ Takes a number, and returns how many letters are in that number's word.
    Ex: the number 'one' (1) has three letters"""
    letters = 0
    num = str(number)

    # Ones
    if len(num) == 1:
        letters = len(ones[number-1])
        return letters

    # Tens
    if len(num) == 2:
        # 10-19
        if number < 20:
            letters = len(teens[number-10])
            return letters
        # Numbers ending in 0. Ex: 20, 30 ,40
        if num[1] == '0':
            letters = len(tens[int(num[0])-2])
            return letters
        letters = len(tens[int(num[0])-2]) + len(ones[int(num[1])-1])
        return letters

    # Hundreds
    if len(num) == 3:
        letters = len(ones[int(num[0])-1]) + 10  # 10 letters in "hundred and..."
        # For multiples of one hundred (200, 500, etc.) we dont use the "and" so -3
        if int(num[1]+num[2]) == 0:
            return letters - 3
        return (letters + add_letters(int(num[1]+num[2])))

    if number == 1000:
        letters = 11  # 11 letters in "one thousand"
        return letters

for i in range(1,1001):
    answer += add_letters(i)

print(answer)
