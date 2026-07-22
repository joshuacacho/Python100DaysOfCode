print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people split the bill? "))

# calculate split bill
tip_bill = bill * (12 / 100)
split_bill = str(round((bill + tip_bill) / people,2))
print("Each person should pay " +  split_bill)


