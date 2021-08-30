import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2) 

if human_choice < 0 or human_choice >= 3:
    print("You typed an invalid number. You lose")
else:
    print(game_images[human_choice])
    print("Computer chose:")
    print(game_images[computer_choice])

  # if human_choice == 0:
  #   if computer_choice == 0:
  #     print("It's a draw")
  #   elif computer_choice == 1:
  #     print("You lose")
  #   else:
  #     print("You win!")
  # elif human_choice == 1:
  #   if computer_choice == 1:
  #     print("It's a draw")
  #   elif computer_choice == 0:
  #     print("You win!")
  #   else:
  #     print("You lose")
  # elif human_choice == 2:
  #   if computer_choice == 2:
  #     print("It's a draw")
  #   elif computer_choice == 1:
  #     print("You win!")
  #   else:
  #     print("You lose")

    if human_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and human_choice == 2:
        print("You lose")
    elif computer_choice > human_choice:
        print("You lose")
    elif human_choice > computer_choice:
        print("You win!")
    elif computer_choice == human_choice:
        print("It's a draw")
