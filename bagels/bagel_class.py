import random

class BagelsGame:
    def __init__(self, num_digits=3, max_guesses=10):
        self.NUM_DIGITS = num_digits
        self._max_guesses = max_guesses  # Make _max_guesses a private attribute

    @property
    def MAX_GUESSES(self):
        return self._max_guesses

    def get_secret_num(self):
        numbers = list('0123456789')
        random.shuffle(numbers)
        return ''.join(numbers[:self.NUM_DIGITS])

    def get_valid_guess(self, num_guesses):
        while True:
            guess = input(f'Guess #{num_guesses}: ')
            if len(guess) == self.NUM_DIGITS and guess.isdecimal():
                return guess
            else:
                print('Invalid guess. Please enter a valid {}-digit number.'.format(self.NUM_DIGITS))

    def get_clues(self, guess, secret_num):
        if guess == secret_num:
            return 'You got it!'

        clues = []

        for i in range(len(guess)):
            if guess[i] == secret_num[i]:
                clues.append('Fermi')
            elif guess[i] in secret_num:
                clues.append('Pico')

        if not clues:
            return 'Bagels'
        else:
            clues.sort()
            return ' '.join(clues)

if __name__ == '__main__':
    bagels_game = BagelsGame()

    print(f'''Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com

    I am thinking of a {bagels_game.NUM_DIGITS}-digit number with no repeated digits.
    Try to guess what it is. Here are some clues:
    When I say:    That means:
      Pico         One digit is correct but in the wrong position.
      Fermi        One digit is correct and in the right position.
      Bagels       No digit is correct.

    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.''')

    while True:
        secret_num = bagels_game.get_secret_num()
        print('I have thought up a number.')
        print(f' You have {bagels_game.MAX_GUESSES} guesses to get it.')

        num_guesses = 1
        while num_guesses <= bagels_game.MAX_GUESSES:
            guess = bagels_game.get_valid_guess(num_guesses)
            clues = bagels_game.get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break

            if num_guesses > bagels_game.MAX_GUESSES:
                print(f'You ran out of guesses. The answer was {secret_num}.')

        play_again = input('Do you want to play again? (yes or no) ').lower()
        if not play_again.startswith('y'):
            break

    print('Thanks for playing!')
