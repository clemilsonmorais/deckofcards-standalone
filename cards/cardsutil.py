CARDS_IMAGES_DIR = '../images/'
CARDS_BASE_NAME = CARDS_IMAGES_DIR + '{code}.png'


def card_to_dict(card):
    value = card[:1]
    suit = card[1:]
    code = value+suit
    d = dict()
    d['code'] = code
    d['image'] = CARDS_BASE_NAME.format(code=code)

    # if value+suit == "AD":
    #    d['image'] = 'http://deckofcardsapi.com/static/img/aceDiamonds.png'
    if value == 'A':
        value = 'ACE'
    elif value == 'J':
        value = 'JACK'
    elif value == 'Q':
        value = 'QUEEN'
    elif value == 'K':
        value = 'KING'
    elif value == '0':
        value = '10'

    if suit == 'S':
        suit = 'SPADES'
    elif suit == 'D':
        suit = 'DIAMONDS'
    elif suit == 'H':
        suit = 'HEARTS'
    elif suit == 'C':
        suit = 'CLUBS'

    d['value'] = value
    d['suit'] = suit

    return d