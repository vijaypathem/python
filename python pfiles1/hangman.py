import random

word_list=["hello","world","hangman","game"]

choose_word=random.choice(word_list)
print(choose_word)
word_length=len(choose_word)
display=[]
lives=6
end_game=False

for _ in choose_word:
    display+="_"
print(display)

while not end_game:
 guess_letter=input("guess a letter:\n").lower()
 if guess_letter in display:
     print(f"you've already guessed this letter:{guess_letter}")

 for position in range(word_length):
     letter=choose_word[position]
     if guess_letter==letter:
         display[position]=letter
 print(display)
 if not "_" in display:
     print("Y0U won")
     end_game=True



 if guess_letter not in choose_word:
     lives-=1
     if lives==0:
         print("you lose the game is over")
         end_game=True

