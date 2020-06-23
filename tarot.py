import pygame, sys, os, random, time
from pygame.locals import *
from tarot_cards import *

pygame.init()
screen = pygame.display.set_mode((950, 650))

# window caption & icon
pygame.display.set_caption('Tarot Card Reading')
icon = pygame.image.load('images/candle.png')
pygame.display.set_icon(icon)

# colors
PURPLE = (15, 16, 74)
GREY = (96, 85, 99)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# fonts & headers
# card_font = pygame.font.SysFont('cochin.ttc', 32)
past_header = pygame.image.load('images/past.png')
pastH_scaled = pygame.transform.scale(past_header, (150, 50))
present_header = pygame.image.load('images/present.png')
presentH_scaled = pygame.transform.scale(present_header, (150, 50))
future_header = pygame.image.load('images/future.png')
futureH_scaled = pygame.transform.scale(future_header, (150, 50))

# placeholder for cards
past = pygame.Rect(150, 110, 200, 350)
present = pygame.Rect(375, 110, 200, 350)
future = pygame.Rect(600, 110, 200, 350)

card_back = pygame.image.load('images/card_back.png')
cb_scale = pygame.transform.scale(card_back, (200, 500))

# display cards - choose at random and scale
past_card = random.choice(tarot_cards)
past_scaled = pygame.transform.scale(past_card, (200, 500))

present_card = random.choice(tarot_cards)
present_scaled = pygame.transform.scale(present_card, (200, 500))

future_card = random.choice(tarot_cards)
future_scaled = pygame.transform.scale(future_card, (200, 500))


# set screen background and place card back images
screen.fill(PURPLE)
screen.blit(pastH_scaled, (173, 50))
screen.blit(presentH_scaled, (395, 50))
screen.blit(futureH_scaled, (623, 50))
screen.blit(cb_scale, past)
screen.blit(cb_scale, present)
screen.blit(cb_scale, future)
pygame.display.update()

# game loop
while True:
        
    pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            screen.fill(GREY)

        if event.type == pygame.MOUSEBUTTONDOWN and past.collidepoint(pos):
            screen.blit(past_scaled, past)

        if event.type == pygame.MOUSEBUTTONDOWN and present.collidepoint(pos):
            screen.blit(present_scaled, present)

        if event.type == pygame.MOUSEBUTTONDOWN and future.collidepoint(pos):
            screen.blit(future_scaled, future)

    pygame.display.update()