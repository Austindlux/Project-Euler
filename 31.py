"""How many different ways can £2 be made using any number of coins"""

coins = [1, 2, 5, 10, 20, 50, 100, 200]
possibilities = []  # Stores how many ways you can get (index)p by using the coins

for i in range(0,201):
    possibilities.append(1) # Using just 1p coin, each amount can be made once

for coin in coins:
    if coin == 1:
        continue

    for i in range(coin, 201):
        num = i - coin
        possibilities[i] += possibilities[num]



print(possibilities[200])