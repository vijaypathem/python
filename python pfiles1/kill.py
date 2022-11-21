import random


def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calc_score(cards):

    if sum(cards)==21 and len(cards)==2:
        return  0

    if 11 in cards and sum(cards)>21:
        cards. remove(11)
        cards.append(1 )

    return sum(cards)

def compare(user_score,com_score):
    if user_score>21 and com_score>21:
        return "you lost"
    elif user_score==com_score:
        return "draw"
    elif com_score==0:
        return "you lost, computer got blackjack"
    elif user_score==0:
        return "you won, you got blackjack"
    elif user_score>21:
        return "you lost, you went over"
    elif com_score>21:
        return "you won, opponent went over"
    elif user_score >com_score:
        return "you won, you got blackjack"

def play_game():
    user_card=[]
    com_card=[]
    is_game_over=False
    for _ in range(2):
        user_card.append(deal_card())
        com_card.append(deal_card())
    while not is_game_over:      

        user_score=calc_score(user_card)
        com_score=calc_score(com_card)
        print(f"your cards: {user_card}")
        print(f"computer first card: {com_card[0]}")

        if user_score==0 or com_score==0 or user_score>21:
            is_game_over =True
        else:
            user_should_deal= input("type 'y' to get another card, type 'n' to pass:\n")
            if user_should_deal=="y":
                user_card.append(deal_card())
            else:
                is_game_over=True

        while com_score !=0 and com_score<17:
            com_card.append(deal_card())
            com_score=calc_score(com_card)
    print(f"your final hand: {user_card}, final score : {user_score}")
    print(f"computers final hand: {com_card}, final score : {com_score}")
    print(compare(user_score,com_score))
while input("do you want to play blackjack? 'y' or 'n'")=="y":
    play_game()