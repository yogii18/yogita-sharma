

import os
import random
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound


def audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

        try:

            word = r.recognize_google(audio)
            return word

        except:
            return "speak again loudly"


def output(sent):
    obj = gTTS(text=sent, lang='en-us', slow=False)
    obj.save('output.mp3')
    playsound('output.mp3', True)
    os.remove('output.mp3')


print("WELCOME TO ROCK PAPER AND SCISSORS GAME BY YOGITA")
# playername=input("Enter your name:")
#("Enter your Name : ", end='')
print("Enter Your Good Name")
name="Enter your good name"
output(name)
name = audio()
print(name)


playerscore = 0
computerscore = 0

print("Enter max_score",end='')
#max_score = int(input('Enter Max Score:'))
max_score = "Enter Max Score"
output(max_score)
max_score = audio()
output(max_score)
print(max_score)

print("rock,paper or scissors")
option = ["ROCK", "PAPER", "SCISSORS"]

while playerscore != max_score and computerscore != max_score:

    # playerinput = input("ROCK,PAPER OR SCISSORS? ")
    print("ROCK,PAPER OR SCISSORS? ",end='')
    playerinput = audio()
    print(playerinput)

    computerinput= random.choice(option)
    print("computer's choice >>",computerinput)

    if playerinput.lower() == computerinput.lower():
        print('Game Tie')
        text = 'Game Tie'
        output(text)
    elif playerinput.lower() == "rock":
         if computerinput.lower() == "paper":
             computerscore += 1
             print("Bad luck You Lost!")
             second_turn = "Bad luck You Lost!"
             output(second_turn)
         else:
             playerscore += 1
             print("YEH YOU WON!!")
             winn = "YEH YOU WON!!"
             output(winn)
    elif playerinput.lower() == "paper":
         if computerinput.lower() == "scissor":
              computerscore += 1
              print("Bad luck You Lost!")
              lostt = "Bad luck You Lost!"
              output(lostt)
         else:
               playerscore += 1
               print("Yeh You Won!")
               wonn = "Yeh You Won!"
               output(wonn)
    elif playerinput.lower() == "scissor":
         if computerinput.lower() == "rock":
            computerscore += 1
            print("Bad luck You Lost!")
            defeat = "Bad luck You Lost!"
            output(defeat)
         else:
           playerscore += 1
           print("Yeh You Won!")
           won = "Yeh You Won!"
           output(won)
    else:
         print("wrong input,check your spelling")
         wrong_input = "wrong input,check your spelling"
         output(wrong_input)
    print("----------------------------------------------------------------")

if playerscore == max_score:
    print("YEAH BRO! You Won the game")
    winner = "YEAH BRO! You Won the game"
    output(winner)
else:
     print("BAD LUCK BRUH! You Lost the Game!")
     bad_luck = "BAD LUCK BRUH! You Lost the Game!"
     output(bad_luck)