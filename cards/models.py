import datetime, json, random, string

_CARDS_IMAGES_DIR = '../images/'
_CARDS_BASE_NAME = _CARDS_IMAGES_DIR + '{code}.png'


def _random_string():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(12))


_CARDS = ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '0S', 'JS', 'QS', 'KS',
          'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '0D', 'JD', 'QD', 'KD',
          'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '0C', 'JC', 'QC', 'KC',
          'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '0H', 'JH', 'QH', 'KH']
_SUITS = {'S': 'Spades', 'H': 'Hearts', 'D': 'Diamonds', 'C': 'Clubs'}
_NAMED_CARDS = {'A': 'Ace', 'J': 'Jack', 'Q': 'Queen', 'K': 'King', '0': '10'}


def _generate_card_list():
    cards = [Card(code) for code in _CARDS]
    return cards


class Deck(object):
    def __init__(self, key=None, stack=None, stack_used=None
                 , piles=None, deck_contents=None):
        self.key = _random_string() if key is None else key
        self.deck_count = 1
        self.stack = [] if stack is None else stack
        self.stack_used = [] if stack_used is None else stack_used
        self.piles = {} if piles is None else piles
        self.deck_contents = deck_contents
        self.shuffled = False

    def create_new(self, deck_count=1, shuffle=False):
        self.deck_count = deck_count
        stack = []
        if self.deck_contents is None:
            cards = _generate_card_list()
        else:
            cards = self.deck_contents[:]
            self.deck_contents = cards[:]  # save the subset for future shuffles

        for i in range(0, self.deck_count):  # for loop over how many decks someone wants. Blackjack is usually 6.
            stack = stack + cards[:]  # adding the [:] forces the array to be copied.
        self.stack = stack
        self.stack_used = []
        if shuffle:
            random.shuffle(self.stack)
            self.shuffled = True

    def draw_cards(self, card_count, cards_to_draw=None):
        drawed_cards = []
        if card_count <= len(self.stack):
            drawed_cards = self.stack[0:card_count]
            self.stack = self.stack[card_count:]
            self.stack_used += drawed_cards
        else:
            pass  # raise error

        return drawed_cards

    def add_to_pile(self, cards, key=_random_string()):
        pile = self.piles.get(key)
        if pile is None:
            self.piles[key] = []
        self.piles[key].extend(cards)
        return key

    def draw_from_pile(self, key, count=1, bottom=True):
        if key is None:
            raise KeyError('Key cannot be None')
        if not bottom:
            count *= -1
        pile = self.piles.get(key)
        if pile is None:
            raise KeyError('Pile from key {k} not found'.format(k=key))
        cards = pile[0:count]
        self.piles[key] = pile[count:]
        return cards

    def shuffle_pile(self, key):
        if self.piles.get(key) is None:
            raise KeyError('Pile not found')
        pile = self.piles.get(key)
        random.shuffle(pile)

    def list_cards_in_pile(self, key):
        if self.piles.get(key) is None:
            raise KeyError('Pile not found')
        return self.piles.get(key)


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.code = value + suit

    def __init__(self, code):
        self.code = code
        self.value = code[:1]
        self.suit = code[1:]

    def get_card_image(self):
        return _CARDS_BASE_NAME.format(code=self.code)

    def get_card_name(self):
        return '{name} of {suit}'.format(name=_NAMED_CARDS.get(self.value, self.value)
                                         , suit=_SUITS.get(self.suit))

    def __str__(self):
        return self.code

    __repr__ = __str__

