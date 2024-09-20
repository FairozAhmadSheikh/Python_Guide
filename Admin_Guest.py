Inventory={
    "Laptop":{"Name":"Lenovo ideapad","Price":2000,"Stock":9},
    "Phone":{"Name":"I-Phone","Price":200,"Stock":10}
}
# Admin Database and Control
who_am_i=input("Are You Admin or Customer! \n").lower()
if who_am_i=="admin":
    password=input("Enter your password : ")
    if password=="Database@123":
        print(Inventory)
    else:
        print("Wrong Password ")
else:
    print(" Press 1 to order a Laptop")
    print(" Press 2 to order a Mobile")

    choice=input(":")
    # Order Laptop
    if choice=="1":
        print("You are Ordering "+Inventory["Laptop"]["Name"]+ ":" +str(Inventory["Laptop"]["Price"])+" RS")
        quantity=int(input("How Many do you want to Order : "))
        if quantity<=int(Inventory["Laptop"]["Stock"]):
            Total_Amount=quantity*int(Inventory["Laptop"]["Price"])
            print("Your Total Amount for ordering "+ str(quantity) +" "+Inventory["Laptop"]["Name"]+" is : ", Total_Amount)
            confirmation=input("Enter Yes to confirm order and NO to cancel ").lower()
            if confirmation=="yes":
                Inventory["Laptop"]["Stock"]-=quantity
                print("Order Sucessfull"," Stock Left in Our Store is : ",Inventory["Laptop"]["Stock"])
            else:
                print("Thanks for Only Having a Look and Missing best Deal on ",Inventory["Laptop"]["Name"])
        else:
                print("We dont Have so much Stock You can order max of : ",Inventory["Laptop"]["Stock"])
            # Order Mobile
    elif choice=="2":
        print("You are Ordering "+Inventory["Phone"]["Name"]+ ":" +str(Inventory["Phone"]["Price"])+" RS")
        quantity=int(input("How Many do you want to Order : "))
        if quantity<=int(Inventory["Phone"]["Stock"]):
            Total_Amount=quantity*int(Inventory["Phone"]["Price"])
            print("Your Total Amount for ordering "+ str(quantity) +" "+Inventory["Phone"]["Name"]+" is : ", Total_Amount)
            confirmation=input("Enter Yes to confirm order and NO to cancel ").lower()
            if confirmation=="yes":
                Inventory["Phone"]["Stock"]-=quantity
                print("Order Sucessfull"," Stock Left in Our Store is : ",Inventory["Phone"]["Stock"])
            else:
                print("Thanks for Only Having a Look and Missing best Deal on ",Inventory["Phone"]["Name"])
        else:
                print("We dont have so much stock left , you can order max of : ",Inventory["Phone"]["Stock"])
    else:
        print("Thanks for visiting our strore")
