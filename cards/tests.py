from cards.models import *
from unittest import TestCase


class CardsTestCase(TestCase):

    def setUp(self):
        pass

    def test_create_new_deck(self):
        deck = Deck()
        deck.create_new(1)

        multiple_deck = Deck()
        multiple_deck.create_new(2)

        multiple_deck_1 = Deck()
        multiple_deck_1.create_new(3)

        self.assertEqual(52, len(deck.stack), 52)
        self.assertEqual(104, len(multiple_deck.stack))
        self.assertEqual(156, len(multiple_deck_1.stack))

    def test_create_shuffled_deck(self):
        normal_deck = Deck()
        shuffled_deck = Deck()

        normal_deck.create_new(shuffle=False)
        shuffled_deck.create_new(shuffle=True)

        self.assertNotEqual([card.code for card in normal_deck.stack],
                            [card.code for card in shuffled_deck.stack])

    def test_draw_cards(self):
        deck = Deck()
        deck.create_new(shuffle=True)
        cards = deck.draw_cards(3)

        self.assertEqual(3, len(cards))
        self.assertEqual(49, len(deck.stack))
        self.assertEqual(3, len(deck.stack_used))

    def test_create_pile(self):
        deck = Deck()
        deck.create_new()
        cards = deck.draw_cards(3)
        pile_key = deck.add_to_pile(cards)

        self.assertEqual(1, len(deck.piles))
        self.assertEqual(3, len(deck.piles[pile_key]))

    def test_draw_from_pile(self):
        deck = Deck()
        deck.create_new()
        cards = deck.draw_cards(3)
        pile_key = deck.add_to_pile(cards)
        card = deck.draw_from_pile(pile_key)

        self.assertIsNotNone(card)
        self.assertEqual(2, len(deck.piles[pile_key]))

    def test_list_cards_in_pile(self):
        deck = Deck()
        deck.create_new()
        pile_key = deck.add_to_pile(deck.draw_cards(5))
        pile_cards = deck.list_cards_in_pile(pile_key)

        self.assertIsNot(0, len(pile_cards))

    def test_shuffle_pile(self):
        deck = Deck()
        deck.create_new()
        cards = deck.draw_cards(5)
        pile_key = deck.add_to_pile(cards)
        deck.shuffle_pile(pile_key)
        shuffled_cards = deck.list_cards_in_pile(pile_key)

        self.assertNotEqual([card.code for card in cards],
                            [card.code for card in shuffled_cards])
