# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Enter a two-digit number. \nThe first digit is the column, the second is the row: ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
column_num = int(position[0])
row_num = int(position[1])

map[row_num - 1][column_num - 1] = "X"

# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
