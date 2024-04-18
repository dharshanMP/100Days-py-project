# BILL Generator
Bill = int(input("Total Bill amt : "))
Tips = int(input("Enter the tips 10, 12, 15: "))
Tip = round((Tips/100) * Bill , 2)
Total = round(Bill + Tip , 2)
people = int(input("how many of them split the bill : "))
final_amt = Total/people
print(f"{Total} bill amt with tips {Tip} each person should pay {final_amt}")




