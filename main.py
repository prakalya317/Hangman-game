from replit import clear
import hangman_art
import hangman_words
import random


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

guessed_letters = []

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    clear()

    if guess in guessed_letters:
      print(f"You have already guessed the letter {guess}.")
    guessed_letters.append(guess)

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
            print("The letter you chose is present in the word")

    if guess not in chosen_word:

        print(f"The letter you guessed {guess}, is not present in the word, you lose a life..")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. Pssst, the solution is {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("YOU WIN!!")
    
    print(hangman_art.stages[lives])
    