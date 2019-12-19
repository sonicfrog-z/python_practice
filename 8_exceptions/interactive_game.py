from abc import ABC, abstractmethod


class InvalidInputException(Exception):
    pass


class InteractiveGame(ABC):
    @abstractmethod
    def get_instruction(self):
        pass

    @abstractmethod
    def get_prompt(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def validate(self, guess):
        pass

    @abstractmethod
    def evaluate(self, valid_guess):
        pass

    @abstractmethod
    def say_congratulations(self):
        pass

    @abstractmethod
    def say_sorry(self):
        pass

    @abstractmethod
    def can_continue(self):
        pass
