import random
from card import Card

class Deck():
    """A deck of cards."""

    NUMBER_CARDS_IN_SUIT = 13

    def __init__(self):
        """Initialize a deck as a list of all 52 cards:

        13 cards in each of the four suits.
        """

        self.__deck = [
            Card(i, j)
            for j in Card.SUIT_LIST
            for i in range(1,Deck.NUMBER_CARDS_IN_SUIT+1)
        ] # list comprehension

    def __str__(self):
        """Returns a string representation of the whole deck."""

        return_str = ""
        for index, card in enumerate(self.__deck):
            if index % Deck.NUMBER_CARDS_IN_SUIT == 0 and index != 0:  # insert newline: print 13 cards per line
                return_str += "\n"  
            return_str += str(card) + " "

        return return_str

    def shuffle(self):
        """Shuffles the deck."""

        random.shuffle(self.__deck) 

    def deal(self):
        """Deal a single card.

        Returns the card that is removed off the top of the deck.
        """

        if len(self.__deck) == 0:  # deck is empty
            return None
        else:
            return self.__deck.pop(0)  # remove card (pop it) and then return it
