import pygame
import time
import random

pygame.init()

crashSound = pygame.mixer.Sound("Crash.wav")
pygame.mixer.music.load("Jazz_In_Paris.wav")
introSound = pygame.mixer.Sound("Tennessee_Hayride.wav")

windowWidth = 1200
windowHeight = 650
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)

brightRed = (255,0,0)
brightGreen = (0,255,0)

green = (0,200,0)
blue = (0,0,255)
blockColor = (53,115,225)
carWidth = 175

window = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("Miss it")
clock = pygame.time.Clock()
carImage = pygame.image.load('Audi-Q2_0.png')         #car.png

pause = False

def thingsDodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score : "+str(count), True, black)
    window.blit(text, (0,0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(window, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    window.blit(carImage,(x,y))

def textObj(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

def messageDisplay(text):
    fontText = pygame.font.Font('freesansbold.ttf',105)
    textSurf, textRect = textObj(text, fontText)
    textRect.center = ((windowWidth/2),(windowHeight/2))
    window.blit(textSurf, textRect)

    pygame.display.update()
    
    time.sleep(2)
    gameLoop()

def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crashSound)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #window.fill(white)
        fontText = pygame.font.Font('freesansbold.ttf',105)
        textSurf, textRect = textObj("You Crashed Buddy", fontText)
        textRect.center = ((windowWidth/2),(windowHeight/2))
        window.blit(textSurf, textRect)

        button("Play Again", 225, 475, 150, 75, green, brightGreen, "Game")
        button("QUIT", 825, 475, 150, 75, red, brightRed, "Quit")
        
        #pygame.draw.rect(window,red,(825,475,150,75))
        
        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if (x+w) > mouse[0] > x and (y+h) > mouse[1] >y:
        pygame.draw.rect(window,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "Play":
                gameLoop()
            elif action == "Quit":
                pygame.quit()
                quit()
            elif action == "Pause":
                unpause()
            elif action == "Game":
                gameLoop()
            
    else:
        pygame.draw.rect(window,ic,(x,y,w,h))


    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf, textRect = textObj(msg, smallText)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    window.blit(textSurf, textRect)

def gameIntro():
    intro = True
    pygame.mixer.Sound.play(introSound)
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        window.fill(white)
        fontText = pygame.font.Font('freesansbold.ttf',105)
        textSurf, textRect = textObj("A bit Racey", fontText)
        textRect.center = ((windowWidth/2),(windowHeight/2))
        window.blit(textSurf, textRect)

        button("GO", 225, 475, 150, 75, green, brightGreen, "Play")
        button("QUIT", 825, 475, 150, 75, red, brightRed, "Quit")
        
        #pygame.draw.rect(window,red,(825,475,150,75))
        
        pygame.display.update()
        clock.tick(15)


def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False
    

def paused():

    pygame.mixer.music.pause()
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        window.fill(white)
        fontText = pygame.font.Font('freesansbold.ttf',105)
        textSurf, textRect = textObj("Paused", fontText)
        textRect.center = ((windowWidth/2),(windowHeight/2))
        window.blit(textSurf, textRect)

        button("Continue", 225, 475, 150, 75, green, brightGreen, "Pause")
        button("QUIT", 825, 475, 150, 75, red, brightRed, "Quit")
        
        #pygame.draw.rect(window,red,(825,475,150,75))
        
        pygame.display.update()
        clock.tick(15)


def gameLoop():
    global pause
    pygame.mixer.Sound.stop(introSound)
    pygame.mixer.music.play(-1)
        
    x = (windowWidth*0.40)
    y = (windowHeight*0.78)
    xChange = 0
    yChange = 0
    dodge = 0

    thingStartx = random.randrange(0, windowWidth)
    thingStarty = -650
    thingSpeed = 5
    thingWidth = 100
    thingHeight = 100

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -5
                elif event.key == pygame.K_RIGHT:
                    xChange = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()
                     
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xChange = 0
        
        x += xChange
               
        window.fill(white)

        #things(thingx, thingy, thingw, thingh, color):
        things(thingStartx, thingStarty, thingWidth, thingHeight, blockColor)
        thingStarty += thingSpeed
        
        car(x,y)
        thingsDodged(dodge)
        
        if x > windowWidth-carWidth or x < 0:
            crash()

        if thingStarty > windowHeight:
            thingStarty = 0-thingHeight
            thingStartx = random.randrange(0,windowWidth)
            dodge += 1

            if thingSpeed < 12:
                thingSpeed += 0.25
                
            if dodge > 10:
                thingWidth = random.randrange(50,175)
                thingHeight = random.randrange(50,175)
            
        if y < thingStarty + (thingHeight/2):
            print("y crossover")
            if x>thingStartx and x<thingStartx+thingWidth or x+carWidth>thingStartx and x+carWidth<thingStartx+thingWidth or x+(carWidth/2)>thingStartx and x+(carWidth/2)<thingStartx+thingWidth:
                print('x crossover')
                crash()
        
        pygame.display.update()             #or pygame.display.flip()
        clock.tick(100)

gameIntro()
gameLoop()
pygame.quit()
quit()
