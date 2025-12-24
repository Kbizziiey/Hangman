import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(chosen_word)

while True:

    guess = input("Guess a letter: ").lower()

    placeholder = ""

    for letter in range(len(chosen_word)):
        placeholder += "_"
        
    # print(placeholder)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            
        else:
            display += "_"
            
    print(display)

    if "_" not in display:
        print("You win!")
