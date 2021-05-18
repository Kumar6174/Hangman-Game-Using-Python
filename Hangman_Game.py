
import random
words = ["skykreeper", "winterland", "starwars"]
chosen_words = random.choice(words)
stages=['''
    <====>
    |    |
    O    |
   /|\   |
   / \   |
         |
============
''', '''
    <====>
    |    |
    O    |
   /|\   |
   /     |
         |
============
''', '''
    <====>
    |    |
    O    |
   /|\   |
         |
         |
============
''', '''
    <====>
    |    |
    O    |
   / \   |
         |
         |
============
''', '''
    <====>
    |    |
    O    |
     \   |
         |
         |
============
''', '''
    <====>
    |    |
    O    |
         |
         |
         |
============
''', '''
    <====>
    |    |
         |
         |
         |
         |
============
''']
# print(chosen_words,"\n")
lives=5
list1=[]
word_length=len(chosen_words)

for _ in range(word_length):
    list1 +="_"

game_end=False
while not game_end:
    guess = input("Guess a letter..\n").lower()
    
    for position in range(word_length):
        letter= chosen_words[position]
        if letter==guess:
            list1[position]=letter
        

    if guess not in chosen_words:
    
        lives -= 1
        if lives==0:
            game_end=True
            print("You Lose!!")

        print(f"{' '.join(list1)}")
            
        print(f"Remaining Lives : {lives}")
        if not "_" in list1:
            game_end=True
            print("You Win!!")
    
    print(stages[lives])