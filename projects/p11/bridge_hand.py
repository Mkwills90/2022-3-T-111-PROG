from card import Card

class BridgeHand():
    """A class for encapsulating a hand in bridge."""

    NUMBER_CARDS = 13
    
    def __init__(self):
        """Initializes an empty bridge hand."""

        self.__cards = [ Card() for i in range(BridgeHand.NUMBER_CARDS)] 

    def __str__(self):
        """A string representation of the hand."""
        
        return_str = ""
        for card in self.__cards:
            return_str += str(card) + " "
        
        return return_str 

    def add_card(self, a_card):
        """Adds the given card to the hand."""

        empty_idx = self.__find_empty_slot()

        # Add the card if an empty slot is founds
        if empty_idx >= 0:
            self.__cards[empty_idx] = a_card
    

    def __find_empty_slot(self):
        """Returns the index of the first empty slot, if any, else -1."""
        
        for idx, card in enumerate(self.__cards):
            if card.is_blank():
                return idx
        
        return -1