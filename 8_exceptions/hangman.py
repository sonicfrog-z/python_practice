from interactive_game import InteractiveGame, InvalidInputException
from random_word import RandomWordGenerator


class Hangman(InteractiveGame):
    def __init__(self):
        self._tries = 8
        self._secret_word = \
            RandomWordGenerator('words5000.txt', 5, 8).random_word
        self._guessed_word_so_far = ['_'] * len(self._secret_word)
        self._used_letters = []

    def get_instruction(self):
        return 'Guess my secret word'

    def get_prompt(self):
        return 'Take a guess: '

    def get_status(self):
        result = 'You have {} {} to guess my word'.format(
            self._tries,
            'chances' if self._tries > 1 else 'chance'
        )
        result += '\n'
        result += 'Used letters: {}'.format(
            ' '.join(self._used_letters)
        )
        result += '\n'
        result += ' '.join(self._guessed_word_so_far)
        return result

    def validate(self, guess):
        if len(guess) != 1:
            raise InvalidInputException('Invalid guess. One letter at a time.')
        elif guess > 'z' or guess < 'a':
            raise InvalidInputException('Invalid guess. Type a lower-case letter.')

        return guess

    def evaluate(self, valid_guess):
        self._used_letters.append(valid_guess)

        got_it = False

        for index, letter in enumerate(self._secret_word):
            if letter == valid_guess:
                got_it = True
                self._guessed_word_so_far[index] = valid_guess

        if '_' not in self._guessed_word_so_far:
            return True, None
        else:
            if not got_it:
                self._tries -= 1
            return False, None

    def say_congratulations(self):
        return 'Congratulations! You have guessed my secret word: {}.'.format(
            self._secret_word
        )

    def say_sorry(self):
        return 'Sorry. My secret word is {}.'.format(
            self._secret_word
        )

    def can_continue(self):
        return self._tries > 0

