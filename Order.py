print("Shopping managment")

Laptop_price = 1200
Laptop_stock=20;
Phone_price=800;
Phone_stock=20;
Total_Orderd=0
discount=0.1
print("what do you want to order ")

user_input=int(input("  Press 1 for Laptop and 2 For Phones"))

if user_input==1:
    quantity=int(input("How many do you want  to order?"))
    if quantity<=Laptop_stock:
        Laptop_stock-=quantity
        orignal_price=Total_Orderd+(quantity*Laptop_price)
        Total_Orderd=Total_Orderd+(quantity*Laptop_price)*discount

        print("Order Suceesfull","Total discount :"+str(Total_Orderd) +"For total of",orignal_price)
        print(Laptop_stock)
    else:
        print("We dont have that much stock")
elif user_input==2:
    quantity=int(input("How many do you want  to order?"))
    
    if quantity<=Phone_stock:
        Phone_stock-=quantity
        orignal_price=Total_Orderd+(quantity*Phone_price)
        Total_Orderd=Total_Orderd+(quantity*Phone_price)*discount
        print("Order Suceesfull","Total discount :"+str(Total_Orderd)+"For total of",orignal_price)
        print(Phone_stock)
    else:
        print("We dont have that much stock")
else:
    print(" Invalid Input enter correct choice")
