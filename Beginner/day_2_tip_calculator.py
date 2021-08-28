#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")

bill_amount = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
person_of_splitting = int(input("How many people to split the bill? "))

total_tip_amount = (100 + tip_percentage) / 100
bill_with_tip = bill_amount * total_tip_amount
bill_per_person = bill_with_tip / person_of_splitting
final_amount = "{:.2f}".format(bill_per_person)
message = f"Each person should pay: ${final_amount}"

print(message)