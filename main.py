import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(chosen_word)

game_over = False

correct_letter = []


while not game_over:

    guess = input("Guess a letter: ").lower()

    placeholder = ""

    for letter in range(len(chosen_word)):
        placeholder += "_"
        
    # print(placeholder)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
            
        elif letter in correct_letter:
            display += letter
                
        else:
            display += "_"
            
    print(display)

    if "_" not in display:
        print("You win!")
