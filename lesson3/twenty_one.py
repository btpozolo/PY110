import pprint
import random as r

def build_deck():
    deck = []
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

    for suit in suits:
            for number in numbers:
                    deck.append([suit, number])

    return deck 

def deal_cards(deck, number_cards):
    hand = []
    for _ in range(number_cards):
        card = r.choice(deck)
        hand.append(card)
        print(f'card dealt: {card}')

        deck.remove(card)
    return hand   

def get_hand_value(hand):
    # check total of hand without aces
    # start with each ace valued at 11
    # if total is greater than 21, change one ace to 1 and recheck
    
    value = 0
    numbers = '2345678910'
    faces_value = 10
    target_value = 21
    initial_ace_value = 11
    updated_ace_value = 1
    
    for card in hand:
        # Number cards are their values
        if card[1] in numbers:
             value += int(card[1])
        # Face values are 10
        elif card[1] != 'A':
             value += faces_value

    # Aces Handling
    aces = [card for card in hand if card[1] == 'A']
    value += (len(aces) * initial_ace_value)

    while value > target_value:
        print(f'Current value = {value}')
        print(f'Num of aces = {len(aces)}')
        if aces:
            value -= (initial_ace_value - updated_ace_value)
            aces.pop()
            continue
        else:
            break

    return value

deck = build_deck()
player_hand = deal_cards(deck, 2)
player_hand += deal_cards(deck, 1)
player_hand.append(['Test', 'A'])

pprint.pprint(f'Players hand is: {player_hand}')
print(f'hand value is: {get_hand_value(player_hand)}')

dealer_hand = deal_cards(deck, 2)
dealer_hand.append(deal_cards(deck, 1))
pprint.pprint(f'Dealers hand is: {dealer_hand}')
print(f'hand value is: {get_hand_value(dealer_hand)}')


#pprint.pprint(f'Current deck is: {deck}')