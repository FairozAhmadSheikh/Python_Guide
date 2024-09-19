Inventory={
    "Laptop":{"Name":"Lenovo ideapad","Price":2000,"Stock":10},
    "Phone":{"Name":"I-Phone","Price":200,"Stock":10}
}
# Admin Database and Control
who_am_i=input("Are You Admin or Guest! \n").lower()
if who_am_i=="admin":
    password=input("Enter your password : ")
    if password=="Database@123":
        print(Inventory)
    else:
        print("Wrong Password ")
else:
    print(" Press 1 to order a Laptop")
    print(" Print 2 to order a Mobile")

    choice=input(":")
    # Order Laptop
    if choice=="1":
        print("You are Ordering "+Inventory["Laptop"]["Name"]+ ":" +str(Inventory["Laptop"]["Price"])+" RS")
        quantity=int(input("How Many do you want to Order : "))
        Total_Amount=quantity*int(Inventory["Laptop"]["Price"])
        print("Your Total Amount for ordering "+ str(quantity) +" "+Inventory["Laptop"]["Name"]+" is : ", Total_Amount)
        confirmation=input("Enter Yes to confirm order and NO to cancel ").lower()
        if confirmation=="yes":
            if quantity<=int(Inventory["Laptop"]["Stock"]):
                Inventory["Laptop"]["Stock"]-=quantity
                print("Order Sucessfull"," Stock Left in Our Store is : ",Inventory["Laptop"]["Stock"])
            else:
                print("We dont Have so much Stock")
        else:
            print("Thanks for Only Having a Look and Missing best Deal on ",Inventory["Laptop"]["Name"])

            # Order Mobile
    elif choice=="2":
        print("You are Ordering "+Inventory["Phone"]["Name"]+ ":" +str(Inventory["Phone"]["Price"])+" RS")
        quantity=int(input("How Many do you want to Order : "))
        Total_Amount=quantity*int(Inventory["Phone"]["Price"])
        print("Your Total Amount for ordering "+ str(quantity) +" "+Inventory["Phone"]["Name"]+" is : ", Total_Amount)
        confirmation=input("Enter Yes to confirm order and NO to cancel ").lower()
        if confirmation=="yes":
            if quantity<=int(Inventory["Phone"]["Stock"]):
                Inventory["Phone"]["Stock"]-=quantity
                print("Order Sucessfull"," Stock Left in Our Store is : ",Inventory["Phone"]["Stock"])
            else:
                print("We dont have so much stock left")
        else:
            print("Thanks for Only Having a Look and Missing best Deal on ",Inventory["Phone"]["Name"])
    else:
        print("Thanks for visiting our strore")