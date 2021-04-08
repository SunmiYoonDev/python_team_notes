change = 3.56
count = 0

# The coins arranged in ascending order
coin_types = [2, 1, 0.25, 0.1, 0.05, 0.01]

for coin in coin_types:
    # Count a maximum number of coins to make change
    count += n // coin 
    n %= coin

print(count)