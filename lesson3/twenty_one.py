import pprint
import random as r
import os

TARGET_VALUE = 21
DEALER_STAYS = 17
LINE_WIDTH = 41

def initialize_deck():
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
        # print(f'card dealt: {card}')

        deck.remove(card)
    return hand   

def display_prompt(message):
    print(f'==> {message}')

def display_card(card, player, action):
    display_prompt(f'{player} {action} {card[0][1]} of {card[0][0]}')

def display_cards(hand, dealer_hand, show_dealers_cards=False):
    os.system('clear')
    print('-' * LINE_WIDTH)
    print('|', ' ' * 14, '21 GAME',' ' * 14,'|' )

    print('-' * LINE_WIDTH)
    if show_dealers_cards:
        display_prompt(f'Dealer has a {get_hand(dealer_hand)}')
    else:
        display_prompt(f'Dealer shows a {dealer_hand[0][1]} of {dealer_hand[0][0]}')
    print('-' * LINE_WIDTH)
    
    cards = get_hand(hand)
    display_prompt(f'You have {cards}')
    display_prompt(f'Your current value is: {get_hand_value(hand)}')

def display_winner(winner):
    print()
    match winner:
        case 'Player':
            display_prompt('Player wins!! Congratulations')
        case 'Dealer':
            display_prompt('Computer wins. Better luck next time!')
        case _:
            display_prompt('The round has ended in a draw.')
    print()

def get_hand(hand):
    cards = []
    for card in hand:
        cards += [" of ".join([card[1], card[0]])]
    return ", ".join(cards)

def get_hand_value(hand):
    # check total of hand without aces
    # start with each ace valued at 11
    # if total is greater than 21, change one ace to 1 and recheck
    
    value = 0
    numbers = '2345678910'
    faces_value = 10
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

    while value > TARGET_VALUE:
        # print(f'Current value = {value}')
        # print(f'Num of aces = {len(aces)}')
        if aces:
            value -= (initial_ace_value - updated_ace_value)
            aces.pop()
            continue
        else:
            break

    return value

def get_player_move():
    print('-' * LINE_WIDTH)
    while True:
        print('    Select move: hit (h) or stand (s)')
        print('-' * LINE_WIDTH)
        selection = input().strip().lower()[0]
        if not selection:
            display_prompt('Please make a selection')
            continue
        if selection in ['h', 's']:
            break
        else:
            display_prompt('Invalid selection')
    return selection

def get_winner(player_hand, dealer_hand):
    player_value = get_hand_value(player_hand)
    dealer_value = get_hand_value(dealer_hand)

    if is_busted(player_hand):
        return 'Dealer'
    elif is_busted(dealer_hand):
        return 'Player'
    else:
        if player_value > dealer_value:
            return 'Player'
        elif player_value < dealer_value:
            return 'Dealer'
        else:
            return 'Draw'

def is_busted(hand):
    return (get_hand_value(hand) > TARGET_VALUE)

def update_hand(hand, move):
    match move:
        case 'h':
            hand += deal_cards(hand, 1)
        case 's':
            return 
        case '_':
            return
    
def play_player_hand(player_hand, deck):
    while True:
        if is_busted(player_hand):
            print()
            display_prompt('Oh no - you busted!')
            return

        move = get_player_move()
        match move:
            case 'h':
                card = deal_cards(deck, 1)
                player_hand += card
                display_card(card, 'You', 'hit and get a')
                print()
                cards = get_hand(player_hand)
                display_prompt(f'You have {cards}')
                display_prompt(f'Your current value is: {get_hand_value(player_hand)}')
                continue
            case 's':
                return 
            case '_':
                return

def play_dealer_hand(dealer_hand, deck):
    display_card([dealer_hand[1]], 'Dealer', 'flips over')
    display_prompt(f'Dealer\'s current value is: {get_hand_value(dealer_hand)}')

    while get_hand_value(dealer_hand) < DEALER_STAYS:
        card = deal_cards(deck, 1)
        dealer_hand += card
        
        print()
        display_card(card, 'Dealer', 'hits and gets a')
        display_prompt(f'Dealer\'s current value is: {get_hand_value(dealer_hand)}')

def play_21():
    while True:
        play_round()

        if not play_again():
            break
    print('Thanks for playing!')

def play_round():
    deck = initialize_deck()

    player_hand = deal_cards(deck, 2)
    dealer_hand = deal_cards(deck, 2)

    display_cards(player_hand, dealer_hand)
    play_player_hand(player_hand, deck)

    if not is_busted(player_hand):
        play_dealer_hand(dealer_hand, deck)

    winner = get_winner(player_hand, dealer_hand)
    display_winner(winner)

def play_again():
    print('-' * LINE_WIDTH)
    print(' Play again? Yes (y) or no (n)')
    print('-' * LINE_WIDTH)
    
    while True:
        selection = input().strip().lower()[0]
        if not selection:
            display_prompt('Please make a selection')
            continue
        if selection in ['y', 'n']:
            break
        else:
            display_prompt('Invalid selection')
    match selection:
        case 'y':
            return True
        case 'n':
            return False



play_21()