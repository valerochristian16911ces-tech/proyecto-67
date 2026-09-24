import pygame
import random
pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])
pygame.display.set_caption('piedra,papel y tijeras')

rock_button = pygame.Rect(SCREEN_WIDTH/4-75, SCREEN_HEIGHT/2, 150, 50)
paper_button = pygame.Rect(SCREEN_WIDTH/2-75, SCREEN_HEIGHT/2, 150, 50)
scissor_button = pygame.Rect(SCREEN_WIDTH-SCREEN_WIDTH/4-75, SCREEN_HEIGHT/2, 150, 50)

grey = (128, 128, 128)
yellow = (253,255,0)
red = (200,0,0)
black = (0,0,0)
green = (0, 255, 0)

clock = pygame.time.Clock()
game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

imp = pygame.image.load("RPS_home_pic.jpg")
imp = pygame.transform.scale(imp, (700,350))

font = pygame.font.Font('freesansbold.ttf', 32)
rock_text = font.render('Rock', True, black)
paper_text = font.render('Paper', True, black)
scissor_text = font.render('Scissor', True, black)
win_text = font.render('You Win', True, green)
tie_text = font.render('Its a Tie', True, yellow)
lose_text = font.render('You Lose', True, red)
computer_text = font.render('', True, black)

pygame.mouse.set_visible(False)

from random import randint


current_number = randint(1000, 3112)