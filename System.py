
# The System.py file contains the basic class definitions for the Blackjack game.
# Each class represents a different aspect of the game.

import random

class Dealer:
    pass

class Player:
    """
    The Player class represents a player in the Blackjack game. 
    It includes attributes for the player's username and bet amount.
    """
    def __init__(self, username, deposit):
        self.username = username
        self.deposit = deposit
        self.deposit_history = []
    
        
class Cards:
    """
    Initialize a new Cards instance. This constructor creates a deck of cards and shuffles it.
    """
    def __init__(self):
        self.decks = self.create_decks()
    
    def create_decks(self):
        """
        Create a standard deck of 52 cards.
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        decks = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(decks)
        
        return decks # Shuffled deck
    
    def one_card(self):
        if self.decks:
            return self.decks.pop()
        
class Checker:
    pass

cards = Cards()
print(cards.decks)