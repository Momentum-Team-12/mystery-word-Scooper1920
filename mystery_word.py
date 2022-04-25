import random
import time

file = open("words.txt","rt")
data = file.read()
words = data.split()
# the above block of code is to open the file and split the words into 
#separate strings. "rt" is the mode.  it means read text
sorrys =["That letter isn't in this word!", "Too bad, so sad, Try again!","Nope! Better luck next time!","Great guess...but not great enough.  Try again!","Nah, playah.  Try again","Nope, tough luck, kiddo. Try again!"]
sorry = random.choice(sorrys)
congratulations =["Winner, Winner, chicken dinner!","Woohoo!  You win!","Yasss!","Way to go!","Get a load a' you! You win!","Omg you are awesome at this!"]
congrats =random.choice(congratulations)
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
            word = word[:index] + removed_character +word[index+1:]
#second number in a slice is where the index after the slice ends.  This line of
#characters will show from position 0 until the caracter before where the index was left
#in line 23 and add the removed character, then continue with the word being sliced from 
#the character AFTER the index going until the end of the word.  This is so
#the same character doesn't keep coming up.
            spaces[index]=guess
#placing the guess in the proper index
        else:
            index = -1
        
        return(word,spaces)

def scoreCheck():
#we are validating the user input here.  returning 1 for every correct letter guess

    for i in range(0, len(spaces)):
        if spaces[i]=="_":
            return -1
    return 1


turns = 8
for i in range(0,9):
    guess =input('Guess a letter!:')
#ask user to add a letter

    if guess in word:
        word,spaces =play_game(guess,word,spaces)
    #using the original function to place the guess and spaces amongst the word
        print(spaces)
    
    else:
        print(random.choice(sorrys) + " You have " + (str(turns -i) +" turns left!"))
    
    if scoreCheck() == 1:
        print(congrats)
        break

    if (turns-i) ==0 and "_" in spaces:
        print("You lost, you bring dishonor to your family")
    
print(" You have" + str(turns-i) + " turn(s) left")
#i wanted to use modulo to reference the variable here but couldn't get it
print()

       

        


if __name__ == "__main__":
    play_game(guess,word,spaces)
