import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images=[paper,scissors,rock]
your_choice=int(input("select your choice 0 for paper,1 for sccissor,2 for rock\n"))
if your_choice<0 or your_choice>=3:
    print("you entered a wrong input: you lose")
else:
    print(game_images[your_choice])
    com_choice=random.randint(0,2)
    print(game_images[com_choice])
    if com_choice==your_choice:
        print("Game Draw")
    elif com_choice==0 and your_choice==2:
        print("YOU LOSE")
    elif com_choice==2 and your_choice==1:
        print("YOU LOSE")
    elif com_choice==1 and your_choice==0:
        print("YOU LOSE")
    else:
        print("YOU WIN")