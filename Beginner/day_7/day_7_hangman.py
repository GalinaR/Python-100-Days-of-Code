import random
from hangman_art import logo, stages
from hangman_words import word_list
from replit import clear # run in replit


print(logo)
lives = len(stages) - 1   # 6 lives

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
display += "_" * word_length

while lives > 0 and "_" in display:
    guess = input("Guess a letter: ").lower()

    # Use the clear() function imported from replit to clear the output between guesses.
    clear()

    if guess in display:
        print(f"You've already guessed {guess}\n")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}\n")

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print("You lose.")
    
    # Check if user has got all letters.
    if "_" not in display:
        print("You win.")

    # print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives]) 