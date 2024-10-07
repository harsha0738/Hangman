import random

# from replit import clear

import hangman_words

from hangman_art import logo
print(logo)

choosen_word = random.choice(hangman_words.word_list).lower()
# print(f"choosen word is {choosen_word}")

lives = 6

display = []

word_length = len(choosen_word)

for letter in range(word_length):
  display  += "_"
print(display)

end_of_game = False


while not end_of_game:
  guess = input("Guess a letter :").lower()
  # clear()

  if guess in display:
    print(f"you already guessed {guess}")
  
  for position in range(word_length):
    letter = choosen_word[position]
    if letter == guess:
      display[position] = guess
    
  print(display)

  if guess not in choosen_word:
    print(f"You've guessed {guess}, and that is not in choosen word. You lose a life")
    lives -= 1
    print(f"you have {lives} lives left")
    from hangman_art import stages
    print(stages[lives])
    if lives <= 0:
      end_of_game = True
      print("you lose")
      print(f"choosen word is {choosen_word}")


  if "_" not in display:
    end_of_game = True
    print("You win")


  



