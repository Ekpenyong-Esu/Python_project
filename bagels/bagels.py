import random

class BagelsGame:
    def __init__(self, digits):
        self.digits = digits
        self.secret_number = self.generate_secret_number()

    def generate_secret_number(self):
        """Generate a random secret number with the specified number of digits."""
        return ''.join(random.sample('0123456789', self.digits))

    def provide_feedback(self, guess):
        """Provide feedback based on the player's guess."""
        if self.secret_number == guess:
            return "Congratulations! You've guessed the correct number."

        clues = []
        for i in range(len(self.secret_number)):
            if guess[i] == self.secret_number[i]:
                clues.append("Fermi")
            elif guess[i] in self.secret_number:
                clues.append("Pico")

        if not clues:
            return "Bagels"

        return ', '.join(clues)

    def play(self):
        """Main function to play the Bagels game."""
        print("Welcome to Bagels!")
        print(f"I've chosen a {self.digits}-digit number. Try to guess it.")

        attempts = 0

        while True:
            player_guess = input("Enter your guess: ")
            attempts += 1

            feedback = self.provide_feedback(player_guess)
            print("Feedback: {}".format(feedback))

            if feedback.startswith("Congratulations"):
                print("It took you {} attempts.".format(attempts))
                break

# Example: Play Bagels with a 3-digit secret number
if __name__ == "__main__":
    bagels_game = BagelsGame(digits=3)
    bagels_game.play()
