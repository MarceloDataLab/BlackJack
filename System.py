
# The System.py file contains the basic class definitions for the Blackjack game.
# Each class represents a different aspect of the game.

import random

class Dealer:
    def __init__(self):
        self.hand = []
    
    def play_hand(self):
        pass    

class Player:
    """
    The Player class represents a player in the Blackjack game. 
    It includes attributes for the player's username and bet amount.
    """
    def __init__(self, username, deposit):
        self.username = username
        self.balance = deposit
        self.deposit_history = []
        self.hand = []
    
    def make_deposit(self,deposit):
        self.balance += deposit
        self.deposit_history.append(deposit)
        
    def play_cards(self):
        pass
    
    def __repr__(self):
        return f"Your balance is {self.balance}$ and your earnings are {self.balance - sum(self.deposit_history)}$"
    
class Cards:
    """
    Initialize a new Cards instance. This constructor creates a deck of cards and shuffles it.
    """
    def __init__(self):
        self.deck = self.create_deck()
    
    def create_deck(self):
        """
        Create a standard deck of 52 cards.
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        decks = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(decks)
        
        return decks # Shuffled deck
    
    def one_card(self):
        if self.deck:
            return self.deck.pop() # it gives one card and take out from shuffled deck
        
class BlackJack:
    def __init__(self, user, deposit):
        self.dealer = Dealer()
        self.player = Player(user, deposit)
        self.cards = Cards()
        
    def check_username(self):
        while not self.player.username  or self.player.username.strip() == "":
            self.player.username = str(input("Username cannot be empty. Please enter a valid username: ")).strip()

    def check_balance(self):
        while self.player.balance < 5:
            print("make a deposit! minimun amount to play is 5$")
            deposit = int(input("how much would you like to deposit? "))
            self.player.make_deposit(deposit)
            print("deposited successfully!")
    
    def start(self):
        self.cards.create_deck()
        self.player.hand.append(self.cards.one_card())
        self.player.hand.append(self.cards.one_card())
        self.dealer.hand.append(self.cards.one_card())
        self.dealer.hand.append(self.cards.one_card())


    def open(self,play_again=True):
        return play_again
      
if __name__ == "__main__":
    user = input(f"insert username: ")
    deposit = int(input(f"insert money here: "))
    game = BlackJack(user, deposit)
    game.check_username()
    game.check_balance()

    game.start()
