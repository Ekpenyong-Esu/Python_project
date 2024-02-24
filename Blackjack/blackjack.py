import random

class BlackjackGame:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

    def create_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
        random.shuffle(deck)
        return deck

    def deal_card(self, hand):
        card = self.deck.pop()
        hand.append(card)

    def calculate_score(self, hand):
        score = sum([self.card_value(card['rank']) for card in hand])
        if 'A' in [card['rank'] for card in hand] and score + 10 <= 21:
            score += 10
        return score

    def card_value(self, rank):
        if rank in ['J', 'Q', 'K']:
            return 10
        elif rank == 'A':
            return 1
        else:
            return int(rank)

    def play_game(self):
        for _ in range(2):
            self.deal_card(self.player_hand)
            self.deal_card(self.dealer_hand)

        game_over = False

        while not game_over:
            player_score = self.calculate_score(self.player_hand)
            dealer_score = self.calculate_score(self.dealer_hand)

            print(f"Your cards: {self.player_hand}, current score: {player_score}")
            print(f"Dealer's first card: {self.dealer_hand[0]}")

            if player_score == 0 or dealer_score == 0 or player_score > 21:
                game_over = True
            else:
                another_card = input("Type 'y' to get another card, 'n' to pass: ")
                if another_card == 'y':
                    self.deal_card(self.player_hand)
                else:
                    game_over = True

        while dealer_score != 0 and dealer_score < 17:
            self.deal_card(self.dealer_hand)
            dealer_score = self.calculate_score(self.dealer_hand)

        print(f"Your final hand: {self.player_hand}, final score: {player_score}")
        print(f"Dealer's final hand: {self.dealer_hand}, final score: {dealer_score}")
        print(self.determine_winner(player_score, dealer_score))

    def determine_winner(self, player_score, dealer_score):
        if player_score > 21:
            return "You went over. You lose."
        elif dealer_score > 21:
            return "Dealer went over. You win!"
        elif player_score == dealer_score:
            return "It's a draw."
        elif player_score == 21:
            return "Blackjack! You win!"
        elif dealer_score == 21:
            return "Dealer has a Blackjack. You lose."
        elif player_score > dealer_score:
            return "You win!"
        else:
            return "You lose."


# Run the game
if __name__ == "__main__":
    blackjack_game = BlackjackGame()
    blackjack_game.play_game()
