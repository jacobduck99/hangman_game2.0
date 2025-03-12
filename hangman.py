import random

def hangman():
    words = ["dog", "dinosaur", "Lebron", "redbull"]
    random_word = random.choice(words)
    coded_word = ["_" for _ in random_word] 
    attempts = 12 

    print("Welcome!")
    print("Type 'quit' to exit the program: ")
    print()
    print(" ".join(coded_word))  

    while True:
        if "_" not in coded_word:
            print(f"🎉 You won! The word was '{random_word}'!")
            break 
        
        if attempts <= 0:
            print("Game over! The word was:", random_word)
            play_again = input("\nDo you want to play again? (yes/no): ").lower()
            if play_again == 'yes':
                hangman()
            else:
                print("Thanks for playing!")
                quit()

        user_input = input("Please enter a letter you think it could be: ").lower()
        attempts -= 1

        if user_input == 'quit':
            break

        for i, letter in enumerate(random_word): 
            if user_input == letter:
                coded_word[i] = letter 

        print(" ".join(coded_word))
        print(f"You have {attempts} attempts left until game over!")

hangman()
