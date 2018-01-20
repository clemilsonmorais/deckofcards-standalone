import sys
# try:
from django.db import models
# except Exception:
#    print("Exception: Django Not Found, please install it with \"pip install django\".")
#    sys.exit()
import datetime, json, random, string
from jsonfield import JSONField


def random_string():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(12))


# Sample User model
class User(models.Model):
    name = models.CharField(max_length=50, default="")

    class Meta:
        db_table = "user_"

    def __str__(self):
        return self.name

    __repr__ = __str__


CARDS = ['AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '0S', 'JS', 'QS', 'KS',
         'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '0D', 'JD', 'QD', 'KD',
         'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '0C', 'JC', 'QC', 'KC',
         'AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '0H', 'JH', 'QH', 'KH']


class Deck(models.Model):
    key = models.CharField(default=random_string, max_length=15, db_index=True)
    last_used = models.DateTimeField(default=datetime.datetime.now)
    deck_count = models.IntegerField(default=1)
    stack = JSONField(null=True, blank=True)
    stack_used = JSONField(null=True, blank=True)
    piles = JSONField(null=True, blank=True)
    deck_contents = JSONField(null=True, blank=True)
    shuffled = models.BooleanField(default=False)

    def open_new(self, cards_used=None):
        stack = []
        if cards_used is None:  # use a subset of a standard deck
            if self.deck_contents is None:
                cards = CARDS
            else:
                cards = self.deck_contents[:]
        else:  # use all the cards
            cards_used = cards_used.upper()
            # Only allow real cards
            cards = [x for x in CARDS if x in cards_used.split(',')]
            self.deck_contents = cards[:]  # save the subset for future shuffles

        for i in range(0, self.deck_count):  # for loop over how many decks someone wants. Blackjack is usually 6.
            stack = stack + cards[:]  # adding the [:] forces the array to be copied.
        self.stack = stack
        self.stack_used = []
        self.last_used = datetime.datetime.now()
        self.save()

    def save(self, *args, **kwargs):
        self.last_used = datetime.datetime.now()
        super(Deck, self).save(*args, **kwargs)
