
# The System.py file contains the basic class definitions for the Blackjack game.
# Each class represents a different aspect of the game.

import random

class Dealer:
    def __init__(self):
        self.hand = []
    
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
    
    def calculate_hand_value(self,cards):
        
        blackjack_values = {'0': 0, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

        count = 0
        num_aces = 0 
        for card in cards:
            count += blackjack_values.get(card[0])
            if blackjack_values.get(card[0]) == "A":
                num_aces += 1
        if num_aces > 0 and count > 21:
            count -= num_aces * 10
        
        return count
         
    def player_play(self):
        value = self.calculate_hand_value(self.player.hand)
        print(f"{self.player.hand} is {value}")
        
        if len(self.player.hand) < 3 and value == 21:
            return 1000
            
        elif self.player.hand[0][0] == self.player.hand[1][0]:
            print("Play Double")
            deck1 = [self.player.hand[0]]
            deck1.append(self.cards.one_card())
            print(f"First hand: {deck1}")
            value = self.calculate_hand_value(deck1)
            if len(deck1) < 3 and value == 21:
                return 1000
            
            while True:
                dec = input("Hit or Stay: ")
                if dec == "stay":
                    break
                elif dec == "hit":    
                    deck1.append(self.cards.one_card())
                    value = self.calculate_hand_value(deck1)
                    print(f"{deck1} is {value}")
                    if value > 21:
                        deck1 = [["0", "0"]]
                        break
                    elif value == 21:
                        return 21
                                  
            deck2 = [self.player.hand[1]]
            deck2.append(self.cards.one_card())
            print(f"second hand: {deck2}")
            
            while True:
                dec = input("Hit or Stay: ")
                if dec == "stay":
                    break
                elif dec == "hit":    
                    deck2.append(self.cards.one_card())
                    value = self.calculate_hand_value(deck2)
                    print(f"{deck2} is {value}")
                    if value > 21:
                        deck2 = [["0", "0"]]
                        break
                    elif value == 21:
                        return 21
                                  
            result_deck1, result_deck2 = self.calculate_hand_value(deck1), self.calculate_hand_value(deck2)
            return max(result_deck1, result_deck2)
        
        else:
            dec = input("Hit or Stay: ")
            if dec == "stay":
                return self.calculate_hand_value(self.player.hand)
            while dec != "stay":
                self.player.hand.append(self.cards.one_card())
                value = self.calculate_hand_value(self.player.hand)
                print(f"{self.player.hand} is {value}")
                if value > 21:
                    return 0
                elif value == 21:
                    return 21
                dec = input("Hit or Stay: ")
            return self.calculate_hand_value(self.player.hand)                
                               
    def dealer_play(self):
        return 19
    
    def check_result(self, result_player, result_dealer):
        pass
    
    def start(self):
        self.cards.create_deck()
        self.player.hand.append(self.cards.one_card())
        self.player.hand.append(self.cards.one_card())
        self.dealer.hand.append(self.cards.one_card())
        self.dealer.hand.append(self.cards.one_card())
        result_player = self.player_play()
        result_dealer = self.dealer_play()
        
    def open(self,play_again=True):
        return play_again
      
if __name__ == "__main__":
    user = input(f"insert username: ")
    deposit = int(input(f"insert money here: "))
    game = BlackJack(user, deposit)
    game.check_username()
    game.check_balance()

    game.start()
