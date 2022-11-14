DEFAULT_RANK = 0
DEFAULT_SUIT = ''

class Card(object):
    """A card with a rank and a suit."""

    RANK_SYMBOL_LIST = ['blk', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']      
    RANK_TO_NUM_DICT = {'J': 11, 'Q': 12, 'K': 13, 'A': 1}
    SUIT_LIST = ['S', 'H', 'D', 'C'] 

    def __init__(self, rank = DEFAULT_RANK, suit = DEFAULT_SUIT): 
        """Initializes a card with the given rank an suit."""

        self.__set_rank(rank)
        self.__set_suit(suit)

        # Make sure both rank and suit have default values if either has default value
        if self.__rank == DEFAULT_RANK or self.__suit == DEFAULT_SUIT:
            self.__rank, self.__suit = DEFAULT_RANK, DEFAULT_SUIT

    def __str__(self):
        """Returns a string representation of card: rank + suit."""

        rank_and_suit = Card.RANK_SYMBOL_LIST[self.__rank] + self.__suit     

        return f"{rank_and_suit:>3s}"

    def __set_rank(self, rank):
        """Sets the rank of the card.

        The rank parameter can either be
        a character or an integer corresponding to the rank.
        Internally, the rank is an integer.
        """

        # rank is int: 1=Ace, 2-10 face value, 11=Jack, 12=Queen, 13=King
        self.__rank = DEFAULT_RANK 
        if type(rank) == str and rank in Card.RANK_TO_NUM_DICT:
            self.__rank = Card.RANK_TO_NUM_DICT[rank]
        elif type(rank) == int:
            if 1 <= rank <= 13:
                self.__rank = rank

    def __set_suit(self, suit):
        """Sets the suit of the card.

        Suit is a character
            S=Space, H=Heart, D=Diamond, C=Club.
        """

        self.__suit = DEFAULT_SUIT
        if type(suit) == str and suit in Card.SUIT_LIST:
            self.__suit = suit

    def is_blank(self):
        return self.__rank == DEFAULT_RANK and self.__suit == DEFAULT_SUIT
