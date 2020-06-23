import os, sys, pygame, random

""" for the card illustrations – CBD Tarot de Marseille by Dr. Yoav Ben-Dov, www.cbdtarot.com 
(with a clickable link when appropriate). you can change the exact formulation, 
but mention the name of the cards, my name and this website address.
Creative Commons by-nc-sa 3.0 license """

magician = pygame.image.load('cards/magician.png')
popess = pygame.image.load('cards/popess.png')
empress = pygame.image.load('cards/empress.png')
emperor = pygame.image.load('cards/emperor.png')
pope = pygame.image.load('cards/pope.png')
lovers = pygame.image.load('cards/lovers.png')
chariot = pygame.image.load('cards/chariot.png')
justice = pygame.image.load('cards/justice.png')
hermit = pygame.image.load('cards/hermit.png')
wheel_fortune = pygame.image.load('cards/wheel_fortune.png')
force = pygame.image.load('cards/force.png')
hanged_man = pygame.image.load('cards/hanged_man.png')
death = pygame.image.load('cards/death.png')
temperance = pygame.image.load('cards/temperance.png')
devil = pygame.image.load('cards/devil.png')
tower = pygame.image.load('cards/tower.png')
"""star = pygame.image.load('cards/star.jpg')
moon = pygame.image.load('cards/moon.jpg')
sun = pygame.image.load('cards/sun.jpg')
judgment = pygame.image.load('cards/judgment.jpg')
world = pygame.image.load('cards/world.jpg')
fool = pygame.image.load('cards/fool.jpg')
 """
""" king_wands = pygame.image.load('cards/king_wands.jpg')
queen_wands = pygame.image.load('cards/queen_wands.jpg')
knight_wands = pygame.image.load('cards/knight_wands.jpg')
knave_wands = pygame.image.load('cards/knave_wands.jpg')

ace_wands = pygame.image.load('cards/ace_wands.jpg')
two_wands = pygame.image.load('cards/two_wands.jpg')
three_wands = pygame.image.load('cards/three_wands.jpg')
four_wands = pygame.image.load('cards/four_wands.jpg')
five_wands = pygame.image.load('cards/five_wands.jpg')
six_wands = pygame.image.load('cards/six_wands.jpg')
seven_wands = pygame.image.load('cards/seven_wands.jpg')
eight_wands = pygame.image.load('cards/eight_wands.jpg')
nine_wands = pygame.image.load('cards/nine_wands.jpg')
ten_wands = pygame.image.load('cards/ten_wands.jpg')

king_cups = pygame.image.load('cards/king_cups.jpg')
queen_cups = pygame.image.load('cards/queen_cups.jpg')
knight_cups = pygame.image.load('cards/knight_cups.jpg')
knave_cups = pygame.image.load('cards/knave_cups.jpg')

ace_cups = pygame.image.load('cards/ace_cups.jpg')
two_cups = pygame.image.load('cards/two_cups.jpg')
three_cups = pygame.image.load('cards/three_cups.jpg')
four_cups = pygame.image.load('cards/four_cups.jpg')
five_cups = pygame.image.load('cards/five_cups.jpg')
six_cups = pygame.image.load('cards/six_cups.jpg')
seven_cups = pygame.image.load('cards/seven_cups.jpg')
eight_cups = pygame.image.load('cards/eight_cups.jpg')
nine_cups = pygame.image.load('cards/nine_cups.jpg')
ten_cups = pygame.image.load('cards/ten_cups.jpg')

king_coins = pygame.image.load('cards/king_coins.jpg')
queen_coins = pygame.image.load('cards/queen_coins.jpg')
knight_coins = pygame.image.load('cards/knight_coins.jpg')
knave_coins = pygame.image.load('cards/knave_coins.jpg')

ace_coins = pygame.image.load('cards/ace_coins.jpg')
two_coins = pygame.image.load('cards/two_coins.jpg')
three_coins = pygame.image.load('cards/three_coins.jpg')
four_coins = pygame.image.load('cards/four_coins.jpg')
five_coins = pygame.image.load('cards/five_coins.jpg')
six_coins = pygame.image.load('cards/six_coins.jpg')
seven_coins = pygame.image.load('cards/seven_coins.jpg')
eight_coins = pygame.image.load('cards/eight_coins.jpg')
nine_coins = pygame.image.load('cards/nine_coins.jpg')
ten_coins = pygame.image.load('cards/ten_coins.jpg')

king_swords = pygame.image.load('cards/king_swords.jpg')
queen_swords = pygame.image.load('cards/queen_swords.jpg')
knight_swords = pygame.image.load('cards/knight_swords.jpg')
knave_swords = pygame.image.load('cards/knave_swords.jpg')

ace_swords = pygame.image.load('cards/ace_swords.jpg')
two_swords = pygame.image.load('cards/two_swords.jpg')
three_swords = pygame.image.load('cards/three_swords.jpg')
four_swords = pygame.image.load('cards/four_swords.jpg')
five_swords = pygame.image.load('cards/five_swords.jpg')
six_swords = pygame.image.load('cards/six_swords.jpg')
seven_swords = pygame.image.load('cards/seven_swords.jpg')
eight_swords = pygame.image.load('cards/eight_swords.jpg')
nine_swords = pygame.image.load('cards/nine_swords.jpg')
ten_swords = pygame.image.load('cards/ten_swords.jpg')
 """

tarot_cards = [
    magician, popess, empress, emperor, pope,
    lovers, chariot, justice, hermit, wheel_fortune,
    force, hanged_man, death, temperance, devil,
   tower ]# star, moon, sun, judgment, world, fool, 

   #"""  king_wands, queen_wands, knight_wands, knave_wands,

   # ace_wands, two_wands, three_wands, four_wands, five_wands,
    #six_wands, seven_wands, eight_wands, nine_wands, ten_wands,

    #king_cups, queen_cups, knight_cups, knave_cups,

    #ace_cups, two_cups, three_cups, four_cups, five_cups,
    #six_cups, seven_cups, eight_cups, nine_cups, ten_cups,

    #king_coins, queen_coins, knight_coins, knave_coins,

   # ace_coins, two_coins, three_coins, four_coins, five_coins,
    #six_coins, seven_coins, eight_coins, nine_coins, ten_coins,

   # king_swords, queen_swords, knight_swords, knave_swords,

  #  ace_swords, two_swords, three_swords, four_swords, five_swords,
#    six_swords, seven_swords, eight_swords, nine_swords, ten_swords
#]
 
""" def meaning_of_card(tarot_cards):
    if past_card or present_card or future_card == magician:
        pygame."Create your own reality. This is the start of something new!")
    if tarot_cards == popess:
        print("Wisdom comes from both your intellect and intution. Trust your instincts.")
    if tarot_cards == empress:
        print("The beauty of the outer world that attracts you is also within yourself. Embrace your own power.")
    if tarot_cards == emperor:
        print("We must critically examine ourselves and take responsibility for our lives. Show leadership.")
    if tarot_cards == pope:
        print("Be open to spiritual teachings. Following your inner guide will lead to the highest transformation.")
    if tarot_cards == lover:
        print("You are wotrthy and ready to give and receive true love in your life.")
    if tarot_cards == chariot:
        print("Put your life in order and face the future with determination abd courage.")
    if tarot_cards == justice:
        print("Be at rest within your own center. Create harmony by bringing balance to your life.")
    if tarot_cards == hermit:
        print("Introspection is necessary. Look within yourself for understanding.")
 """

