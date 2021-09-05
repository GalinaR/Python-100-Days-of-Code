from art import logo


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    letters_amount = len(alphabet)
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "decode":
                new_position = position - shift_amount
            elif cipher_direction == "encode":
                new_position = position + shift_amount
                if new_position >= letters_amount:
                    new_position = new_position % letters_amount # To avoid IndexError if shift will be grater than the number of letters in the alphabet.
            end_text += alphabet[new_position]
        else:
            end_text += char # Don't lose characters other than letters.
    print(f"Here's the {direction}d result: {end_text}\n")

# print the logo.
print(logo)
should_continue = "yes" 

while should_continue == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    should_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
print("Goodbye")
