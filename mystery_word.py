import random
import time

file = open("words.txt","rt")
data = file.read()
words = data.split()
# the above block of code is to open the file and split the words into 
#separate strings. "rt" is the mode.  it means read text
word=random.choice(words)
spaces = ["_"]*len(word)
#the above code matches the "_" string to each random word it pulls and applies
#the correct number of spaces

def play_game(guess, word, spaces):
#this is a suggestion i found online.  an index of -2 will start at the position that is 
#second to last then bump to the last but later in the code it is written to go back to
#the negative 2 position.  
    index = -2
    while index != -1:
#This loop will check every character for the guess.  If it's there we are removing
#the character and putting it in the space that is at the index of the guess"
        if guess in word:
            index = word.find(guess)
            removed_character="*"
#to indicate that the character has been removed from the word
            word = word[:index] +removed_character +word[index+1:]
#second number in a slice is where the index after the slice ends.  This line of
#code will start from position 0 until the caracter before where the index was left
#in line 23 and add the removed character, then continue with the word being sliced from 
#the character AFTER the index going until the end of the word


if __name__ == "__main__":
    play_game()
