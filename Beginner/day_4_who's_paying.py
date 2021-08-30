import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# Get the total number of items in list
count_names = len(names)
random_number = random.randint(0, count_names - 1)
person_who_will_pay = names[random_number]

print(person_who_will_pay + " is going to buy the meal today!")
