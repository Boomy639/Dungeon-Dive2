import pygame # imports pygame

pygame.init() # initializes pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
clock = pygame.time.Clock()    # clock function, how many times the screen is refreshed per second
fps = 120 # traditional fps values, frames per second, right now, its 120

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE) # MAKES GAME WINDOW, sets dimensions and weather its resizable or not
pygame.display.set_caption('Dungeon Dive')
player = pygame.Rect((300, 250, 50, 50)) # this is the player, pygame.Rect() creates a rectangle, but it takes FOUR ARGUMENTS

# FIRST TWO, ARE THE X and Y CO-ORDINATES
# SECOND TWO, ARE THE WIDTH AND HEIGHT

running = True

while running:     # GAME LOOP
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), player) # you're drawing the rectangle to the SCREEN variable, then asigning RGB color codes to it
    # Also apparently this rect has to be lower case, for whatever fucking reason

    key = pygame.key.get_pressed() # this assigns the key variable, and looks for the key that is being pressed
    if key[pygame.K_a] == True:          # If key, inside pygame, is the A key being pressed
        player.move_ip(-1, 0) # IP stands for In Place   -1, 0,   YOU ARE SUBTRACTING FROM THE X COORDINATE, BUT LEAVING THE Y COORDINATE ALONE
    elif key[pygame.K_d] == True:      
        player.move_ip(1, 0)      # This time moves positive X coordinate, also, ELSE IF, ELIF
    elif key[pygame.K_w] == True:         
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:          # THESE TWO, opposite, you are checking the Y co ordinates  
        player.move_ip(0, 1)        # POSITIVE MOVES DOWN, NEGATIVE MOVES UP



    for event in pygame.event.get():
        if event.type == pygame.QUIT:    # EVENT HANDLER5
            running = False

    
    pygame.display.update()
    clock.tick(fps) # uupdate the game "fps" times per second

pygame.quit()