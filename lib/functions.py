import pygame, os, random
from lib import logger

# We need pygame to able to do anything.

pygame.init()

def value(name_of_card):
    name_of_card = str(name_of_card)
    print("PAYLOAD:", name_of_card)
    if name_of_card.startswith('2'):
        print(" RETURN VALUED:", 2)
        return 2
    if name_of_card.startswith('3'):
        print(" RETURN VALUED:", 3)
        return 3
    if name_of_card.startswith('4'):
        print(" RETURN VALUED:", 4)
        return 4
    if name_of_card.startswith('5'):
        print(" RETURN VALUED:", 5)
        return 5
    if name_of_card.startswith('6'):
        print(" RETURN VALUED:", 6)
        return 6
    if name_of_card.startswith('7'):
        print(" RETURN VALUED:", 7)
        return 7
    if name_of_card.startswith('8'):
        print(" RETURN VALUED:", 8)
        return 8
    if name_of_card.startswith('9'):
        print(" RETURN VALUED:", 9)
        return 9
    if name_of_card.startswith('10'):
        print(" RETURN VALUED:", 10)
        return 10
    if name_of_card.startswith('jack'):
        return 11
    if name_of_card.startswith('queen'):
        return 12
    if name_of_card.startswith('king'):
        return 13
    return 14


def loaded_card(name_of_card):
    direc = 'assets/cards/' + name_of_card
    value_of_card = value(name_of_card)
    return pygame.image.load(direc), value_of_card

def load_card(name_of_card):
    direc = 'assets/cards/' + name_of_card + '.png'
    logger.card(name_of_card, "loaded")
    return pygame.image.load(direc)

def random_card():
    all_cards = os.listdir('assets/cards')
    random_card = random.choice(all_cards) # this gets a random card from the images
    logger.system(random_card)
    return random_card


def lose(num):
    logger.info("===========================")
    logger.info("       BLACK JACK          ")
    logger.info("       YOU LOST!!          ")
    logger.info(num)
    logger.info("                           ")
    logger.info("===========================")


# below is a dealer class, that will handle dealer stuff 

class dealer():
    # not rigged at all....
    def random_card(level):
        if(level == 1):
            ez_cards = ["king_of_clubs", "king_of_diamonds", "king_of_hearts", "queen_of_clubs", "queen_of_diamonds", "queen_of_hearts", "queen_of_spades", "jack_of_clubs", "jack_of_diamonds", "jack_of_hearts", "jack of spades", "10_of_clubs", "10_of_diamonds", "10_of_hearts", "10_of_spades"]
            not_rigged = random.choice(ez_cards)
            print("LEVEL 1 ", not_rigged)
            return not_rigged # the dealer will get high cards.
        if(level == 2):
            medium_cards = ["placeholder","placeholder"]
            not_rigged = random.choice(medium_cards)
            return not_rigged
        if(level == 3):
            # this is the hardest one where the bot will ALWAYS GET THE BEST CARDS.
            hard_cards = ["placeholder", "placeholder"]
            not_rigged = random.choice(hard_cards)
            return not_rigged
        return "Yo no bot level was provided"