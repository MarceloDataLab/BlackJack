import random

# Dealer class manages the dealer's hand in the game
class Dealer:
    def __init__(self):
        # Initialize the dealer's hand as an empty list
        self.hand = []
    
# Player class encapsulates all player-related data
class Player:
    """
    The Player class represents a player in the Blackjack game. 
    It stores the player's username, balance, deposit history, and current hand.
    """
    def __init__(self, username, deposit):
        self.username = username
        self.balance = deposit
        self.deposit_history = []
        self.hand = []
    
    # Method to add funds to the player's balance
    def make_deposit(self, deposit):
        self.balance += deposit
        self.deposit_history.append(deposit)

    # String representation for the player showing balance and net gain/loss
    def __repr__(self):
        return f"Your balance is {self.balance}$ and your earnings are {self.balance - sum(self.deposit_history)}$"
    
# Cards class manages a deck of playing cards
class Cards:
    """
    The Cards class is responsible for creating and managing a deck of cards.
    """
    def __init__(self):
        self.deck = self.create_deck()
    
    # Creates and shuffles a standard deck of 52 playing cards
    def create_deck(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        deck = [(rank, suit) for suit in suits for rank in ranks]
        random.shuffle(deck)
        return deck
    
    # Removes and returns one card from the deck
    def one_card(self):
        if self.deck:
            return self.deck.pop()

# BlackJack class encapsulates the game logic
class BlackJack:
    def __init__(self, user, deposit):
        self.dealer = Dealer()
        self.player = Player(user, deposit)
        self.cards = Cards()
    
    # Ensures username is not empty
    def check_username(self):
        while not self.player.username or self.player.username.strip() == "":
            self.player.username = input("Username cannot be empty. Please enter a valid username: ").strip()

    # Ensures player has a minimum balance to play
    def check_balance(self):
        while self.player.balance < 5:
            print("Make a deposit! Minimum amount to play is $5.")
            deposit = int(input("How much would you like to deposit? "))
            self.player.make_deposit(deposit)
            print("Deposited successfully!")
    
    # Calculates the value of a hand of cards
    def calculate_hand_value(self, cards):
        values = {'0': 0, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        total = 0
        aces = 0
        for card in cards:
            total += values[card[0]]
            if card[0] == "A":
                aces += 1
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    # Manages the player's actions during their turn
    def player_play(self):
        total = self.calculate_hand_value(self.player.hand)
        print(f"{self.player.hand} is {total}")
        
        if len(self.player.hand) < 3 and total == 21:
            return 1000  # Blackjack!
        
        # Allow player to hit or stay
        while True:
            decision = input("Hit or Stay: ").lower()
            if decision == "stay":
                break
            elif decision == "hit":
                self.player.hand.append(self.cards.one_card())
                total = self.calculate_hand_value(self.player.hand)
                print(f"{self.player.hand} is {total}")
                if total > 21:
                    return 0  # Bust
                elif total == 21:
                    return 21  # 21, not necessarily blackjack
        return total

    # Manages the dealer's actions based on the player's result
    def dealer_play(self, player_result):
        total = self.calculate_hand_value(self.dealer.hand)
        print(f"Dealer's hand {self.dealer.hand} is {total}")
        
        while total < 17:  # Dealer must hit until they reach at least 17
            self.dealer.hand.append(self.cards.one_card())
            total = self.calculate_hand_value(self.dealer.hand)
            print(f"Dealer's hand {self.dealer.hand} is {total}")
            if total > 21:
                return 0  # Dealer busts
        return total
    
    # Starts a new game of blackjack
    def start(self):
        self.cards.create_deck()
        self.player.hand = [self.cards.one_card(), self.cards.one_card()]
        self.dealer.hand = [self.cards.one_card(), self.cards.one_card()]
        player_result = self.player_play()
        if player_result == 1000:
            return "Blackjack for player!"
        elif player_result == 21:
            return "21, you win!"
        
        dealer_result = self.dealer_play(player_result)
        if player_result > dealer_result:
            return "You win!"
        elif dealer_result > player_result:
            return "Dealer wins!"
        else:
            return "Draw!"

if __name__ == "__main__":
    user = input("Insert username: ")
    deposit = int(input("Insert money here: "))
    game = BlackJack(user, deposit)
    game.check_username()
    game.check_balance()
    while True:
        result = game.start()
        print(result)
        game.player.hand = []
        game.dealer.hand = []
        dec = input("Would you like to play again? (y/n): ")
        if dec.lower() == 'n':
            break
        else:
            game.check_balance()
