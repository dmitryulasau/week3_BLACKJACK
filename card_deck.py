from random import shuffle
import os
from time import sleep

from colorama import Fore, Style, init, Back
init()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# CARDS
suits = ('♥', '♦', '♠', '♣')
ranks = (
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '10',
    'J',
    'Q',
    'K',
    'A'
)
values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,
    'A': 11, # or 1
}

game = True

class Card():

    def __init__(self, suit, rank):
        """Defining a playing CARD"""
        self.suit = suit
        self.rank = rank
    
    def __repr__(self):
        """Showing a CARD"""
        return f"|{self.rank} {self.suit}|"

# DECK
class Deck():
    
    def __init__(self):
        """Creating a DECK of cards"""
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle_deck(self):
        """Shuffle the DECK"""
        shuffle(self.deck)

    def deal(self):
        """Distribute a CARD"""
        one_card = self.deck.pop()
        return one_card

# Hand
class Hand():
    def __init__(self):
        """Cards that player have"""
        self.cards = []
        self.value = 0
        self.ace = 0

    def get_card(self, card):
        """Getting a card"""
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'A':
            self.ace += 1

    def ace_11_or_1(self):
        while self.value > 21 and self.ace:
            self.value -= 10
            self.ace -= 1

# HIT STAND
def hit(deck, hand):
    hand.get_card(deck.deal())
    hand.ace_11_or_1()

def hit_stand(deck, hand):
    global game

    while True:
        answer = input(f"\n{Fore.YELLOW}({Fore.RED}{Style.BRIGHT}'H'{Style.RESET_ALL} {Fore.YELLOW}- HIT) or ({Style.RESET_ALL}{Fore.RED}{Style.BRIGHT}'S'{Style.RESET_ALL} {Fore.YELLOW}- STAND?){Style.RESET_ALL} ")
        if answer[0].lower() == 'h':
            
            hit(deck, hand)
            clear_screen()
        elif answer[0].lower() == 's':
            clear_screen()
            print('DEALER is playing...')
            sleep(1)
            clear_screen()
            game = False
        else:
            print("*** Wrong input. Please follow the instructions! ***")
            continue
        break

def show_cards(player, dealer):
    print(f"\n{Fore.BLUE}{Style.BRIGHT}YOUR CARDS:{Style.RESET_ALL} {Fore.BLACK}{Back.WHITE}{player.cards}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}{Style.BRIGHT}VALUE{Style.RESET_ALL}: {Fore.BLACK}{Back.YELLOW}{Style.BRIGHT} {player.value} {Style.RESET_ALL}")

    
    print(f"\n{Fore.CYAN}{Style.BRIGHT}DEALER CARDS: {Style.RESET_ALL} {Fore.BLACK}{Back.WHITE}[|%%%|, {dealer.cards[0]}]{Style.RESET_ALL}")


def show_cards_all(player, dealer):
    print(f"\n{Fore.BLUE}{Style.BRIGHT}YOUR CARDS:{Style.RESET_ALL} {Fore.BLACK}{Back.WHITE}{player.cards}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}{Style.BRIGHT}VALUE{Style.RESET_ALL}: {Fore.BLACK}{Back.YELLOW}{Style.BRIGHT} {player.value} {Style.RESET_ALL}")

    print(f"\n{Fore.CYAN}{Style.BRIGHT}DEALER CARDS: {Style.RESET_ALL} {Fore.BLACK}{Back.WHITE}{dealer.cards}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Style.BRIGHT}VALUE: {Style.RESET_ALL}{Fore.BLACK}{Back.YELLOW}{Style.BRIGHT} {dealer.value} {Style.RESET_ALL}")
    
def player_lost(player, dealer):
    print(f"\n{Fore.RED}{Style.BRIGHT}-= YOU LOST! =-{Style.RESET_ALL}")

def player_win(player, dealer):
    print(f"\n{Fore.GREEN}{Style.BRIGHT}-= YOU WON! =-{Style.RESET_ALL}")

def tie(player, dealer):
    print(f"\n{Fore.BLUE}{Style.BRIGHT}-= IT'S A TIE =-{Style.RESET_ALL}")
    



while True:
        clear_screen()
        print("DECK SHUFFLING... PLEASE WAIT")
        sleep(2)

        clear_screen()
        
        print(f"{Fore.RED}{Back.WHITE} ♥ {Style.RESET_ALL} {Fore.RED}{Back.WHITE} ♦ {Style.RESET_ALL} {Fore.WHITE}{Style.BRIGHT}*** BLACKJACK ***{Style.RESET_ALL}  {Fore.BLACK}{Back.WHITE} ♠ {Style.RESET_ALL} {Fore.BLACK}{Back.WHITE} ♣ {Style.RESET_ALL}\n")
        deck = Deck()
        deck.shuffle_deck()

        player_hand = Hand()
        player_hand.get_card(deck.deal())
        player_hand.get_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.get_card(deck.deal())
        dealer_hand.get_card(deck.deal())

        show_cards(player_hand, dealer_hand)

        while game:
            hit_stand(deck, player_hand)

            clear_screen()
            show_cards(player_hand, dealer_hand)

            if player_hand.value > 21:
                player_lost(player_hand, dealer_hand)
                break

        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            clear_screen()
            show_cards_all(player_hand, dealer_hand)

            if dealer_hand.value > 21:
                player_win(player_hand, dealer_hand)
            elif dealer_hand.value > player_hand.value:
                player_lost(player_hand, dealer_hand)
            elif dealer_hand.value < player_hand.value:
                player_win(player_hand, dealer_hand)
            else:
                tie(player_hand, dealer_hand)

        again = input(f"\n{Fore.MAGENTA} PLAY AGAIN? (Y/N) {Style.RESET_ALL}")
        if again[0].lower() == 'y':
            game = True
            
            continue
        else:
            clear_screen()
            print(f"\n{Fore.RED}{Back.WHITE} ♥ {Style.RESET_ALL} {Fore.RED}{Back.WHITE} ♦ {Style.RESET_ALL} {Fore.WHITE}{Style.BRIGHT}*** THANKS FOR PLAYING! ***{Style.RESET_ALL}  {Fore.BLACK}{Back.WHITE} ♠ {Style.RESET_ALL} {Fore.BLACK}{Back.WHITE} ♣ {Style.RESET_ALL}")
            
            break


        

