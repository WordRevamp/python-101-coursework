bill_amount = float(input("Enter Total Bill Amount:"))
tip_amount = float(input("Enter Tip Percentage:"))

tip_percentage = tip_amount / 100
user_tip_amount = round(bill_amount * tip_percentage, 2)
total_bill = user_tip_amount + bill_amount

print(f"Tip Calculator\n\nResults:\n\nTip amount = ${user_tip_amount}\nYour total bill is ${total_bill}")

