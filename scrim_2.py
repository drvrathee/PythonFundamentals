#random module

import random

# below is a list of tuples with word paired with a hint for the word ,
#  such a thing can be used n scramble to give hint to player when asked for 

word_bank = [
    ("standup", "Every morning, our fifteen-minute ____ meeting lasts until lunch."),
    ("syntax", "One missing bracket, and Python hits me with a ____ error."),
    ("debug", "I spent four hours trying to ____ my code. Turns out I was missing comma."),
    ("deploy", "It's Friday at 5pm, definitely the best time to ____ new code."),
    ("bandwidth", "Sorry boss, I can't take on more work. I just don't have the ____."),
    ("meeting", "That ninety-minute ____ could have been an email."),
    ("deadline", "Of course we'll hit the ____, no problem! Well, within a couple of days. Maybe a week."),
    ("backup", "We finally made a ____ of everything, the day after the laptop died."),
    ("server", "I'm getting a 500 error, which means the ____ is down again."),
    ("prototype", "It's just an early ____, so please ignore that clicking anywhere crashes it."),
]

total_rounds = 5
round_num = 1
used =[]

print("-" * 30)
print("     WELCOME TO JARGON JUMBLE")
print('-' * 30)

score = 0

while round_num <= total_rounds:

    word , hint = random.choice(word_bank) # picking random words and appending used words in 'used' list.
    while (word,hint) in used:
        word,hint =random.choice(word_bank)
    used.append((word,hint))

    letters = list(word) # jumbling the word taken and giving it to user
    random.shuffle(letters)
    scram_word = "".join(letters)
    print()
    print(f"ROUND-{round_num}")
    print()
    
    print(f"Here's a word for you : {scram_word.lower()} ")
    print()
    guess = input("Guess the word: ( type 'skip' to skip and 'hint' for a hint): ").strip().lower()

    if guess == "hint".strip(): # we give hint and let user guess again
        print(f"{hint}")
        guess = input("Your guess or ('skip') : ").strip().lower()

    if guess == 'quit':
        print(f"The word was {word}")
        break
    
    elif guess == "skip": 
        print(f"Skipped , the word was {word}")
    
    elif guess== word:
        print("Correct✅     +2 points")
        score += 2

    elif guess != word:
        print(f"the word was {word}.")
    
    else: print(f"the word was {word}. You did'nt guess .  +0 points")

    round_num += 1

print(f"your total points are : {score}")


# if the total rounds exceeds or equals the number of words . it will not be good