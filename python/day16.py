def get_price(item):
    if item == 1:
        return 21
    elif item == 2:
        return 17
    elif item == 3:
        return 13
    elif item == 4:
        return 10
    else:
        return 0
total=0
add="no"

while add == "no":
    pass
else:
    print("\n---MENU---")
    print("1.Burger:$21")
    print("2.Pizza:$17")
    print("3.French fries:$13")
    print("4.Taco:$10")
    item=int(input("Enter the item number:"))
    quantity=int(input("Enter the quantity:"))

    price=get_price(item)
    amount=price*quantity
    print("Item amount:",amount)
    total+=amount
    add=input("Add more amount(yes/no):")
coupon=input("Do you have coupon code(save10/no)")
discount=0
if coupon == "save10":
    discount=total*0.10
    after_discount=total-discount
    gst=after_discount*0.05
    final_price=after_discount+gst
print("\n===FINAL BILL===")
print("Total bill:",total)
print("Discount",discount)
print("GST:",gst)
print("Final price:",final_price) 
  

























 
