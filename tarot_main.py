import pygame, sys, os, random, time
from pygame.locals import *
from tarot_cards import *

pygame.init()
screen = pygame.display.set_mode((950, 700))

# window caption & icon
pygame.display.set_caption('Tarot Card Reading')
icon = pygame.image.load('images/candle.png')
pygame.display.set_icon(icon)

# colors
PURPLE = (15, 16, 74)
GREY = (96, 85, 99)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def game_start():
    
    # fonts & headers
    past_header = pygame.image.load('images/past.png')
    pastH_scaled = pygame.transform.scale(past_header, (150, 50))
    present_header = pygame.image.load('images/present.png')
    presentH_scaled = pygame.transform.scale(present_header, (150, 50))
    future_header = pygame.image.load('images/future.png')
    futureH_scaled = pygame.transform.scale(future_header, (150, 50))

    # placeholder for cards
    past = pygame.Rect(140, 110, 200, 350)
    present = pygame.Rect(365, 110, 200, 350)
    future = pygame.Rect(590, 110, 200, 350)

    card_back = pygame.image.load('images/card_back.png')
    cb_scale = pygame.transform.scale(card_back, (200, 500))

    # display cards - choose at random and scale
    past_card = random.choice(tarot_cards)
    past_scaled = pygame.transform.scale(past_card, (200, 500))

    present_card = random.choice(tarot_cards)
    present_scaled = pygame.transform.scale(present_card, (200, 500))

    future_card = random.choice(tarot_cards)
    future_scaled = pygame.transform.scale(future_card, (200, 500))

    # buttons
    restart = pygame.Rect(810, 625, 120, 50)
    r_button = pygame.image.load('images/restart.png')
    r_scaled = pygame.transform.scale(r_button, (120, 50))

    # info = pygame.Rect(810, 650, 120, 50)
    # i_button = pygame.image.load('images/info.png')
    # i_scaled = pygame.transform.scale(i_button, (120, 50))

    # blit screen background and place card back images & buttons
    screen.fill(PURPLE)
    # cards
    screen.blit(pastH_scaled, (163, 50))
    screen.blit(presentH_scaled, (388, 50))
    screen.blit(futureH_scaled, (613, 50))
    screen.blit(cb_scale, past)
    screen.blit(cb_scale, present)
    screen.blit(cb_scale, future)
    # buttons
    screen.blit(r_scaled, restart)
    # screen.blit(i_scaled, info)

    pygame.display.update()

    #game loop
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

            if event.type == pygame.MOUSEBUTTONDOWN and restart.collidepoint(pos):
                game_start()

        pygame.display.update()

game_start()
