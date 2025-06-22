import time

coins = [50, 25, 10, 5, 2, 1]

# Жадібний алгоритм
def find_coins_greedy(amount):
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

# Динамічне програмування
def find_min_coins(amount):
    min_coins = [0] + [float('inf')] * amount
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin
    return result

# Тестування
amount = 113
print("Greedy:", find_coins_greedy(amount))
print("DP:", find_min_coins(amount))

# Порівняння ефективності
large_amount = 10000
start = time.time()
find_coins_greedy(large_amount)
end = time.time()
greedy_time = end - start

start = time.time()
find_min_coins(large_amount)
end = time.time()
dp_time = end - start

print(f"Час жадібного алгоритму: {greedy_time:.6f} с")
print(f"Час динамічного програмування: {dp_time:.6f} с")


