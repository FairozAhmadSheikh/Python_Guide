# Wallet balance 
wallet = 50066

Shop_name="SAMEERS KITCHEN"

# Menu prices
pizza_price = 500
burger_price = 200
hamburger_price = 300

while True:
    print(Shop_name.center(30,"="))
    print("Your Wallet Balance is: $", wallet)
    print("1. Pizza Price: $", pizza_price)
    print("2. Burger Price: $", burger_price)
    print("3. Hamburger Price: $", hamburger_price)
    print("".center(30,"="))

    # Ask user for choice 
    choice = input("\nWhat do you want to order? ( \n1 for Pizza, \n2 for Burger, \n3 for Hamburger 'exit' to exit): ").lower()

    if choice == "1":
        if wallet >= pizza_price:
            wallet -= pizza_price
            print("Order successful! You ordered a Pizza.")
        else:
            print("Not enough money.")
    elif choice == "2":
        if wallet >= burger_price:
            wallet -= burger_price
            print("Order successful! You ordered a Burger.")
        else:
            print("Not enough money.")
    elif choice == "3":
        if wallet >= hamburger_price:
            wallet -= hamburger_price
            print("Order successful! You ordered a Hamburger.")
        else:
            print("Not enough money.")
    elif choice == 'exit':
        print("Thank you for visiting! Goodbye.")
        break
    else:
        print("Invalid choice! Please choose again.")

    # Show remaining balance
    if wallet > 0:
        print("Remaining Wallet Balance: $", wallet)
    else:
        print("Your wallet is empty! No more orders can be placed.")
        break
