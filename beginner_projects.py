# Container
PYHTON | BEGINNER PROJECTS FOR YOU

PROJECT 1 : MAD LIB 
-------------------------

print("MAD LIB GAME IS STARTING!")
print("***************************")

noun1=input("Enter a noun : ")
noun2=input("Enter another noun : ")
noun3=input("Enter another noun : ")
noun4=input("Enter another noun : ")
verb_ing=input("Enter a verb ending in ing : ")
adj=input("Enter an adjective : ")
fm=input("Enter a family member: ")
verb=input("Enter a verb: ")
number=input("Enter a number: ")
ing=input("Enter an ingredient : ")

print("\nEvery year we make " + noun1 +" at Chrismastime.\n" + verb_ing + " has been a tradition since I was a/an " +adj+" kid!")
print( fm+" used to make most of the recipe back then but I would always help\n" + verb+" "+ing+ ".")
print("Now that I am older,I make the entire batch of " + noun2 +" from scratch.\n All you have to do is mix " + noun3 + " and " +noun4+" in a bowl until fluffy and add "+noun1+".")
print("Don't forget the " + noun3 +"!\n" + verb + " them on a " +noun2+" and bake them at "+number+" degrees.")
print("After " + number +" minutes you will have a perfect " + noun4+"!")

PROJECT 2 : NUMBER GUESSING
  ------------------------------
import random
import math

print("NUMBER GUESSING IS STARTING!")
print("Can you find the selected number?")
print("                    -I think noo:)")
print("*************************************\n Please give the lower and upper bound.")

lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper - lower + 1, 2)), " chances to guess the integer!\n")

count = 0

while count < math.log(upper - lower + 1, 2):
    count += 1
    guess = int(input("Guess a number:- "))
    if x == guess:
       print("Congratulations you did it in ", count, " try")
       break
    elif x > guess:
           print("You guessed too small!")
    elif x < guess:
          print("You Guessed too high!")

if count >= math.log(upper - lower + 1, 2):
  print("\nThe number is %d" % x)
print("\t Better Luck Next time!")

PROJECT 3 : TEXT-BASED ADVENTURE
-------------------------------------
name = input("What is your name? ")
age = int(input("What is your age? "))

health = 10

if age >= 18:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are staring with", health, "health")
        print("Let's play!")

        left_or_right = input("First choice... Left or Right (left/right)? ").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)? ")

            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "across":
                print("You managed to get across, but were bit by a fish and lost 5 health.")
                health -= 5

            ans = input("You notice a house and a river. Which do you go to (river/house)? ")
            if ans == "house":
                print("You go to the house and are greeted by the owner... He doesn't like you and you lose 5 health")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you lost the game...")
                else:
                    print("You have survived... You win!")

            else:
                print("You fell in the river and lost...")


        else:
            print("You fell down and lost...")

    else:
        print("Cya...")
else:
    print("You are not old enough to play...")
    
    
    
PROJECT 4 : DICE ROLLING
-----------------------------

import random
low=1
upp=6

again= True

while again:
    print(random.randint(low,upp))
    print(random.randint(low,upp))
    
    another=input("Do you want rolling again?").lower()
    
    if another=="yes" or another=="y":
        continue
    else:
        break

PROJECT 5 : HANGMAN
-----------------------------
import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # listeden rastgele bir kelime seçilir/ a random word from the list
    while '-' in word or ' ' in word:
    word = random.choice(words)

    return word.upper()
  
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # kelimedeki harfler / letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # kullanıcı ne tahmin etmiş / what the user has guessed

    lives = 6

    # kullanıcıdan girdi alalım / getting user input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # kelime nedir (örn. K-L İ M E ) / what current word is (ie. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # yanlış cevapsa bir can eksilir / takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()
    
