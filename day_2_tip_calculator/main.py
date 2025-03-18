# This is a simple program that calculates tip amount based on the bill, tip percentage which is either 10%, 12% or 15%
# and total no of persons to split the bill with. The output will say how much should each pay.

print("Welcome to the tip calculator!")
bill_total = float(input("What is the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15 "))
persons_total = int(input("How many people to split the bill? "))

# calculate total amount after tip
bill_total = bill_total + (0.01 * tip_percent) * bill_total

# calculate how much should each pay
split_bill = round((bill_total / persons_total), 2)

# print the output
print(f"Each person should pay: ${split_bill}")
