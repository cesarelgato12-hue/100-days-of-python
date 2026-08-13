import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']





word_list = ["aardvark","baboon","camel"]


chosen_word = random.choice(word_list)
print(chosen_word)


#aqui se configura el numero de veces que saldrán los espacios de acuerdo a las letras y las posiciones
lives = 6



placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)


game_over = False
correct_letters = []


while not game_over:
     guess = input("Guess a letter:  ").lower()
     display = ""
 #esta parte le pertenece a la letra a colocar y que se ejecute en la pantalla 
     for letter in chosen_word:
         if letter == guess:
           display += letter
           correct_letters.append(guess)
         elif letter in correct_letters:
           display += letter
         else:
           display += "_"

     print (display)



     if guess not in chosen_word:
      lives -= 1
      if lives == 0:
        game_over = True
        print("You lose.")



     if "_" not in display:
      game_over = True    
      print("You win")


     #aqui se configura el arte con el codigo 

     print(stages[6 - lives])

