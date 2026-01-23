print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $").strip())
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
final_bill = (bill/people * (1 + percentage_tip/100))
final_bill_rounded = "{:.2f}".format(final_bill)

print(f"Each person should pay: ${final_bill_rounded}")
