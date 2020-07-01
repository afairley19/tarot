import os, sys, pygame, random

""" Card Illustrations:

    Title: CBD Tarot de Marseille
    Author: Dr. Yoav Ben-Dov
    Date: Accessed June 2020
    Creative Commons by-nc-sa 3.0 license
    Website: www.cbdtarot.com 

"""
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
star = pygame.image.load('cards/star.png')
moon = pygame.image.load('cards/moon.png')
sun = pygame.image.load('cards/sun.png')
judgment = pygame.image.load('cards/judgment.png')
world = pygame.image.load('cards/world.png')
fool = pygame.image.load('cards/fool.png')

king_wands = pygame.image.load('cards/king_wands.png')
queen_wands = pygame.image.load('cards/queen_wands.png')
knight_wands = pygame.image.load('cards/knight_wands.png')
knave_wands = pygame.image.load('cards/knave_wands.png')

ace_wands = pygame.image.load('cards/ace_wands.png')
two_wands = pygame.image.load('cards/two_wands.png')
three_wands = pygame.image.load('cards/three_wands.png')
four_wands = pygame.image.load('cards/four_wands.png')
five_wands = pygame.image.load('cards/five_wands.png')
six_wands = pygame.image.load('cards/six_wands.png')
seven_wands = pygame.image.load('cards/seven_wands.png')
eight_wands = pygame.image.load('cards/eight_wands.png')
nine_wands = pygame.image.load('cards/nine_wands.png')
ten_wands = pygame.image.load('cards/ten_wands.png')

king_cups = pygame.image.load('cards/king_cups.png')
queen_cups = pygame.image.load('cards/queen_cups.png')
knight_cups = pygame.image.load('cards/knight_cups.png')
knave_cups = pygame.image.load('cards/knave_cups.png')

ace_cups = pygame.image.load('cards/ace_cups.png')
two_cups = pygame.image.load('cards/two_cups.png')
three_cups = pygame.image.load('cards/three_cups.png')
four_cups = pygame.image.load('cards/four_cups.png')
five_cups = pygame.image.load('cards/five_cups.png')
six_cups = pygame.image.load('cards/six_cups.png')
seven_cups = pygame.image.load('cards/seven_cups.png')
eight_cups = pygame.image.load('cards/eight_cups.png')
nine_cups = pygame.image.load('cards/nine_cups.png')
ten_cups = pygame.image.load('cards/ten_cups.png')

king_coins = pygame.image.load('cards/king_coins.png')
queen_coins = pygame.image.load('cards/queen_coins.png')
knight_coins = pygame.image.load('cards/knight_coins.png')
knave_coins = pygame.image.load('cards/knave_coins.png')

ace_coins = pygame.image.load('cards/ace_coins.png')
two_coins = pygame.image.load('cards/two_coins.png')
three_coins = pygame.image.load('cards/three_coins.png')
four_coins = pygame.image.load('cards/four_coins.png')
five_coins = pygame.image.load('cards/five_coins.png')
six_coins = pygame.image.load('cards/six_coins.png')
seven_coins = pygame.image.load('cards/seven_coins.png')
eight_coins = pygame.image.load('cards/eight_coins.png')
nine_coins = pygame.image.load('cards/nine_coins.png')
ten_coins = pygame.image.load('cards/ten_coins.png')

king_swords = pygame.image.load('cards/king_swords.png')
queen_swords = pygame.image.load('cards/queen_swords.png')
knight_swords = pygame.image.load('cards/knight_swords.png')
knave_swords = pygame.image.load('cards/knave_swords.png')

ace_swords = pygame.image.load('cards/ace_swords.png')
two_swords = pygame.image.load('cards/two_swords.png')
three_swords = pygame.image.load('cards/three_swords.png')
four_swords = pygame.image.load('cards/four_swords.png')
five_swords = pygame.image.load('cards/five_swords.png')
six_swords = pygame.image.load('cards/six_swords.png')
seven_swords = pygame.image.load('cards/seven_swords.png')
eight_swords = pygame.image.load('cards/eight_swords.png')
nine_swords = pygame.image.load('cards/nine_swords.png')
ten_swords = pygame.image.load('cards/ten_swords.png')
 

tarot_cards = [
    magician, popess, empress, emperor, pope,
    lovers, chariot, justice, hermit, wheel_fortune,
    force, hanged_man, death, temperance, devil,
    tower, star, moon, sun, judgment, world, fool, 

    king_wands, queen_wands, knight_wands, knave_wands,
    ace_wands, two_wands, three_wands, four_wands, five_wands,
    six_wands, seven_wands, eight_wands, nine_wands, ten_wands,

    king_cups, queen_cups, knight_cups, knave_cups,
    ace_cups, two_cups, three_cups, four_cups, five_cups,
    six_cups, seven_cups, eight_cups, nine_cups, ten_cups,

    king_coins, queen_coins, knight_coins, knave_coins,
    ace_coins, two_coins, three_coins, four_coins, five_coins,
    six_coins, seven_coins, eight_coins, nine_coins, ten_coins,
    
    king_swords, queen_swords, knight_swords, knave_swords,
    ace_swords, two_swords, three_swords, four_swords, five_swords,
    six_swords, seven_swords, eight_swords, nine_swords, ten_swords 
]
