from lib import functions, logger
import os, random, pygame


# project started on 2024-10-10
# wanted different files doing different things.

pygame.init()
screen = pygame.display.set_mode((1000, 500))
clock = pygame.time.Clock()
running = True 

print(" ======================= CONFIG ===========================")

bot_dif = int(input("Before starting. Bot difficulty [1-3]: "))

print(" =================================================================")

debug = False # turn on to make it debug mode. more logging in console. verbose.

# debug mode doesn't do anything. The default mode IS debug mode.


# start the main game loop

pygame.display.set_caption('Blackjack hopefully it works plz it work')

background = pygame.image.load('assets/backjack.jpg')
background = pygame.transform.scale(background, (1000, 500))
screen.blit(background, (0,0))

# CARDS LOADING NOW STARTS

print("========== 2 =============")

two_of_clubs = functions.load_card('2_of_clubs')
two_of_diamonds = functions.load_card('2_of_diamonds')
two_of_hearts = functions.load_card('2_of_hearts')
two_of_spades = functions.load_card('2_of_spades')

print("========== 3 =============")

three_of_clubs = functions.load_card('3_of_clubs')
three_of_diamonds = functions.load_card('3_of_diamonds')
three_of_hearts = functions.load_card('3_of_hearts')
three_of_spades = functions.load_card('3_of_spades')

print("========== 4 =============")

four_of_clubs = functions.load_card('4_of_clubs')
four_of_diamonds = functions.load_card('4_of_diamonds')
four_of_hearts = functions.load_card('4_of_hearts')
four_of_spades = functions.load_card('4_of_spades')

print("========== 5 =============")

five_of_clubs = functions.load_card('5_of_clubs')
five_of_diamonds = functions.load_card('5_of_diamonds')
five_of_hearts = functions.load_card('5_of_hearts')
five_of_spades = functions.load_card('5_of_spades')

print("========== 6 =============")

six_of_clubs = functions.load_card('6_of_clubs')
six_of_diamonds = functions.load_card('6_of_diamonds')
six_of_hearts = functions.load_card('6_of_hearts')
six_of_spades = functions.load_card('6_of_spades')

print("========== 7 =============")

seven_of_clubs = functions.load_card('7_of_clubs')
seven_of_diamonds = functions.load_card('7_of_diamonds')
seven_of_hearts = functions.load_card('7_of_hearts')
seven_of_spades = functions.load_card('7_of_spades')

print("========== 8 =============")

eight_of_clubs = functions.load_card('8_of_clubs')
eight_of_diamonds = functions.load_card('8_of_diamonds')
eight_of_hearts = functions.load_card('8_of_hearts')
eight_of_spades = functions.load_card('8_of_spades')

print("========== 9 =============")

nine_of_clubs = functions.load_card('9_of_clubs')
nine_of_diamonds = functions.load_card('9_of_diamonds')
nine_of_hearts = functions.load_card('9_of_hearts')
nine_of_spades = functions.load_card('9_of_spades')

print("========== 10 =============")

ten_of_clubs = functions.load_card('10_of_clubs')
ten_of_diamonds = functions.load_card('10_of_diamonds')
ten_of_hearts = functions.load_card('10_of_hearts')
ten_of_spades = functions.load_card('10_of_spades')

print("========== JACK =============")

jack_of_clubs = functions.load_card('jack_of_clubs')
jack_of_diamonds = functions.load_card('jack_of_diamonds')
jack_of_hearts = functions.load_card('jack_of_hearts')
jack_of_spades = functions.load_card('jack_of_spades')

print("========== QUEEN =============")

queen_of_clubs = functions.load_card('queen_of_clubs')
queen_of_diamonds = functions.load_card('queen_of_diamonds')
queen_of_hearts = functions.load_card('queen_of_hearts')
queen_of_spades = functions.load_card('queen_of_spades')

print("========== KING =============")

king_of_clubs = functions.load_card('king_of_clubs')
king_of_diamonds = functions.load_card('king_of_diamonds')
king_of_hearts = functions.load_card('king_of_hearts')
king_of_spades = functions.load_card('king_of_spades')

print("========== ACE =============")

ace_of_clubs = functions.load_card('ace_of_clubs')
ace_of_diamonds = functions.load_card('ace_of_diamonds')
ace_of_hearts = functions.load_card('ace_of_hearts')
ace_of_spades = functions.load_card('ace_of_spades')


logger.system("All cards loaded, starting game.")

# we need a random system to get 2 images from the directory.

logger.info("Player's hand:")
first_card = functions.random_card()
second_card = functions.random_card()

image_first_card = functions.loaded_card(first_card)
image_second_card = functions.loaded_card(second_card)

# [0] = name of card
# [1] = value of card


print("VALUE OF BOTH CARDS: ", image_first_card[1] + image_second_card[1])

print(first_card, " + ", second_card)

# functions.value(image_first_card)


first_card_rec = image_first_card[0].get_rect()
first_card_rec.x = 100 # same for here but X
first_card_rec.y = 100 # starting pos Y 

second_card_rec = image_second_card[0].get_rect()
second_card_rec.x = 400
second_card_rec.y = 100




logger.info("Dealer's hand:")

dealer_first_card = functions.dealer.random_card(bot_dif)
dealer_second_card = functions.dealer.random_card(bot_dif)


print("== 1 ", dealer_first_card, " ==")
print("== 2 ", dealer_second_card, " ==")


logger.info("Everything is completed, starting game.")
logger.system("=========================================")
logger.system("           BLACKJACK                     ")
logger.system("                                         ")
logger.system("                                         ")
logger.system("                                         ")
logger.system("                                         ")
logger.system("                                         ")
logger.system("           CONTROLS                      ")
logger.system(" ─ SPACE = HIT (YOU WANT ANOTHER CARD)   ")
logger.system(" ─ ENTER = STAND (YOU DON'T WANT ANYCARD)")
logger.system("=========================================")


#all_cards = os.listdir('assets/cards')
#random_card = random.choice(all_cards) # this gets a random card from the images
#logger.system("A random card has been chosen.")



##########################
while running:
   screen.blit(image_first_card[0], first_card_rec)
   screen.blit(image_second_card[0], second_card_rec)
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False
   
   # screen.fill("")


   pygame.display.flip()
   clock.tick(60)
pygame.quit()
