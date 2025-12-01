item = ("bread", "milk", "coffee", "eggs", "rice")
price = ("40", "30", "120", "60", "80")

def showmenu():
    print ("Welcome to the Python Mart!")
    print("Available items:")
    for i in range(len(item)):
        print(f"{i + 1}. {item[i]} - ${price[i]}")

def calculate_bill(cart):
    total = 0
    for i in cart:
        total += int(i[1])
    return total

def main():
    showmenu()
    cart = []
    while True:
        choice = int(input("Enter item number to add to cart (0 to checkout): "))
        if choice == 0:
            break
        elif 1 <= choice <= len(item):
            quantity = int(input(f"Enter quantity of {item[choice - 1]}: "))
            for _ in range(quantity):
                cart.append((item[choice - 1], price[choice - 1]))
            print(f"{item[choice - 1]} added to cart.")
        else:
            print("Invalid choice. Please try again.")
    

    total_bill = calculate_bill(cart)
    print("Your cart items:")
    for i in cart:
        print(f"- {i[0]}: ${i[1]}")
    if total_bill > 500:
        discount = total_bill * 0.1
        total_bill -= discount
        print(f"Discount applied: ${discount:.2f}")    
    print(f"Total bill: ${total_bill}")
    print("Thank you for shopping at Python Mart!")

main()