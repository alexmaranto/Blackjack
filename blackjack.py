import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()

class Player:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def calculate_hand_value(self):
        hand_value = 0
        num_aces = 0

        for card in self.hand:
            if card.rank.isnumeric():
                hand_value += int(card.rank)
            elif card.rank in ["Jack", "Queen", "King"]:
                hand_value += 10
            elif card.rank == "Ace":
                hand_value += 11
                num_aces += 1

        # Adjust for Aces
        while num_aces > 0 and hand_value > 21:
            hand_value -= 10
            num_aces -= 1

        return hand_value

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player()

    def deal_initial_cards(self):
        self.deck.shuffle()
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

    def display_player_hand(self):
        print("Player's Hand:")
        for card in self.player.hand:
            print(f"  {card}")

    def display_partial_dealer_hand(self):
        print("Dealer's Hand:")
        print(f"  {self.dealer.hand[0]}")
        print("  [Hidden Card]")

    def player_turn(self):
        while True:
            self.display_player_hand()
            player_choice = input("Would you like to Hit or Stand? ").lower()
            if player_choice == "hit":
                self.player.add_card(self.deck.deal_card())
                if self.player.calculate_hand_value() > 21:
                    print("Bust! You went over 21. Dealer wins.")
                    return
            elif player_choice == "stand":
                return

    def dealer_turn(self):
        while self.dealer.calculate_hand_value() < 17:
            self.dealer.add_card(self.deck.deal_card())
        print("\nDealer's Hand:")
        for card in self.dealer.hand:
            print(f"  {card}")

    def determine_winner(self):
        player_value = self.player.calculate_hand_value()
        dealer_value = self.dealer.calculate_hand_value()

        print("\nGame Over!")
        print(f"\nPlayer's Hand Value: {player_value}")
        print(f"Dealer's Hand Value: {dealer_value}")

        if player_value > 21:
            print("Bust! You went over 21. Dealer wins.")
        elif dealer_value > 21:
            print("Dealer busts! You win.")
        elif player_value == dealer_value:
            print("It's a tie!")
        elif player_value == 21:
            print("Blackjack! You win.")
        elif dealer_value == 21:
            print("Dealer has Blackjack. Dealer wins.")
        elif player_value > dealer_value:
            print("You win!")
        else:
            print("Dealer wins.")

def play_blackjack():
    game = Game()
    game.deal_initial_cards()
    
    print("Welcome to the table, my friend!\n")
    game.display_partial_dealer_hand()
    game.player_turn()

    if game.player.calculate_hand_value() <= 21:
        game.dealer_turn()
        game.determine_winner()

if __name__ == "__main__":
    play_blackjack()
