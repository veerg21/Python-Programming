import random
print("This is Hangman online")
name=input("Enter your name: ")
print("Good luck", name+"!")
words=['abruptly', 'banjo', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 'fjord', 'flapjack', 'flopping', 'fluffiness', 'flyby']
word=random.choice(words)
# askew
# avenue
# awkward
# axiom
# azure
# bagpipes
# bandwagon
# banjo
# bayou
# beekeeper
# bikini
# blitz
# blizzard
# boggle
# bookworm
# boxcar
# boxful
# buckaroo
# buffalo
# buffoon
# buxom
# buzzard
# buzzing
# buzzwords
# caliph
# cobweb
# cockiness
# croquet
# crypt
# curacao
# cycle
# daiquiri
# dirndl
# disavow
# dizzying
# duplex
# dwarves
# embezzle
# equip
print(word)
turns=6
guesses=''
while turns>0:
    fail=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print("__")
            fail+=1
            print(fail)
    if fail==0:
        print("Congratulations! You won!")
    guess=input("Guess a character: ")
    guesses+=guess
    if guess not in word:
        turns-=1
        print ("This character is not in the word. You have ", turns, "turns left")
        if turns==0:
            print("Better luck next time")
