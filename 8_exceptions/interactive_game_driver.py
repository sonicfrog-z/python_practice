from interactive_game import InteractiveGame, InvalidInputException


class InteractiveGameDriver:
    def __init__(self, game):
        if not isinstance(game, InteractiveGame):
            raise ValueError('Invalid game')
        self._game = game

    def play(self):
        print(self._game.get_instruction())

        while self._game.can_continue():
            print(self._game.get_status())

            guess = input(self._game.get_prompt())
            try:
                valid_guess = self._game.validate(guess)
                result, hint = self._game.evaluate(valid_guess)

                if result:
                    break
                elif hint is not None:
                    print(hint)

            except InvalidInputException as err:
                print(err)

        if result:
            print(self._game.say_congratulations())
        else:
            print(self._game.say_sorry())


if __name__ == '__main__':
    from hangman import Hangman
    dr = InteractiveGameDriver(Hangman())
    dr.play()