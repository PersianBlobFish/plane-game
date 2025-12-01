coke = 50
total = 0
accepted_coins = (25, 15, 10, 5, 1)
print("Amount Due: 50 cents")

while total < coke:
    coin = int(input("Insert coin: "))
    if coin in accepted_coins:
        total += coin
        print("Accepted coin:", coin)
        if total < coke:
            print(f"Amount Due: {coke - total} cents")
    else:
        print("Coin not accepted")

print("Change Owed:", total - coke, "cents")