import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses somthing from the list
    while '-' in word or ' ' in word:
       word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase) #ascii func returns a string containing a printable representation of an object and escapes the non ascii characters in string
    used_letters = set() #what the user has guessed

    lives = 6

    #getting user input
    while len(word_letters) >  0 and lives > 0:
        #letters used
        #' '.join(['a', 'b','cd']) ---> 'a b cd

        print("you have", lives ,"you have used thses letters: ',' ".join(used_letters))

        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        user_letter = input('guess a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1 #takes away a life if wrong
                print('letter is not in word.')

        elif user_letter in used_letters:
            print("you have alread used that character. please try again")

        else:
            print('invalid character. please try again.')



    if lives == 0:
        print("you died. sorry")
    else:
        print("you guessed the word," )

if __name__=='__main__':
    hangman()