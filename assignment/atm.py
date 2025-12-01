balance = 1000.0

print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter choice: "))

match choice:
    case "1":
        print(f"Your balance is ${balance}")
    case "2":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"${amount} deposited. New balance is ${balance}")
        else:
            print("Deposit amount must be positive.")
    case "3":
        amount = float(input("Enter amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"${amount} withdrawn. New balance is ${balance}")
        elif amount > balance:
            print("Insufficient funds!")
        else:
            print("Withdrawal amount must be positive.")
    case "4":
        print("Exiting. Thank you for using the ATM.")
    case _:
        print("Invalid choice. Please try again.")
