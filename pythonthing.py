import pygame
from pygame import mixer
pygame.init()

 
#setting the screen display
#the height and width of screen (can change this as much as needed)
width = 1400
height = 800

# Colors (can add more colors)
black = (0, 0, 0)
white = (255, 255, 255)
gay = (128, 128, 128)

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption("sick beats")

#Can use a differnt ttf file for the text (it basically changes the style of the text oon said game)
#also the number is for the text size but I might keep mmine lage so that antone can see it
label_font = pygame.font.Font('freesansbold.ttf', 32)

#fps is the frame rate
fps = 60
timer= pygame.time.Clock()

def draw_grid():
    left_box = pygame.draw.rect(screen, gay, [0, 0, 200, height], 5)
    bottome_box = pygame.draw.rect(screen, gay [0, height -200, width, 200], 5)
    boxes = []
    colors = {gay, white, gay}


#executess the code times poer sec.
run = True
while run: 
    timer.tick(fps) 
    screen.fill (black)

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.quit:
            run = False
             
    pygame.display.flip()
pygame.quit() 
#opening and closing game
#I may need to change quite to all caps
 
