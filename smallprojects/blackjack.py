import random


# Section creates the card deck properly and assigns the values to them.
# Ace worth 11 AND 1 is only thing not happening here, just 11.

class Card:
    def __init__(self, name, value):
        self.name = name
        self.value = value

suit = ["club", "diamond", "heart", "spade"]
name = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
value = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10, "A":11}

card_deck = []

for suits in suit:
    for names in name:
        card_deck.append(Card(names, value[names]))

print(len(card_deck))

def play_blackjack(card_deck):

    global value

    hand_player = []
    hand_house = []

    score_player = []
    score_house = []

    while len(hand_player) < 2:

        new_card = random.choice(card_deck)
        hand_player.append(new_card)
        card_deck.remove(new_card)

        if len(hand_player) == 2:
            if hand_player[0].value == 11 and hand_player[1].value == 11:
                hand_player[0].value = 1
                score_player -= 10