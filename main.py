"""
PROJET CARGAME VERSION FINALE DEVELOPPE PAR KHARBACH BILAL

"""
from typing import BinaryIO

import pygame
pygame.init()
gray=(119,118,110)
black=(0,0,0)
red=(255,0,0)
green=(0,200,0)
blue=(0,0,200)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)
display_width=800
display_height=600
import time
import random
import pickle
import pathlib






gamedisplays=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("car game")
clock=pygame.time.Clock()
carimg=pygame.image.load('car1.jpg')
backgroundpic=pygame.image.load("download12.jpg")
yellow_strip=pygame.image.load("yellow strip.jpg")
strip=pygame.image.load("strip.jpg")
intro_background=pygame.image.load("background.jpg")
instruction_background=pygame.image.load("background2.jpg")
car_width=56
file = pathlib.Path("save.pkl")
pause=False


""""Le main menu"""
def intro_loop():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(intro_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',115)
        TextSurf,TextRect=text_objects("CAR GAME",largetext)
        TextRect.center=(400,100)
        gamedisplays.blit(TextSurf,TextRect)
        button("START",150,520,100,50,green,bright_green,"play")
        button("LOAD",550,520,100,50,red,bright_red,"load")
        button("INSTRUCTIONS",300,520,200,50,blue,bright_blue,"intro")
        pygame.display.update()
        clock.tick(50)

""""Définition des actions du joueur"""

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+w>mouse[0]>x and y+h>mouse[1]>y:
        pygame.draw.rect(gamedisplays,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=="play":
                countdown()
            elif action=="intro":
                introduction()
            elif action=="menu":
                intro_loop()
            elif action=="pause":
                paused()
            elif action=="unpause":
                unpaused()
            elif action=="load":
                game_load()


    else:
        pygame.draw.rect(gamedisplays,ic,(x,y,w,h))
    smalltext=pygame.font.Font("freesansbold.ttf",20)
    textsurf,textrect=text_objects(msg,smalltext)
    textrect.center=((x+(w/2)),(y+(h/2)))
    gamedisplays.blit(textsurf,textrect)

""""Définition des instructions """

def introduction():
    introduction=True
    while introduction:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()
        gamedisplays.blit(instruction_background,(0,0))
        largetext=pygame.font.Font('freesansbold.ttf',80)
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        mediumtext=pygame.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects("Esquivez les voitures en face de vous pour eviter un accident",smalltext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_objects("INSTRUCTION",largetext)
        TextRect.center=((400),(100))
        gamedisplays.blit(TextSurf,TextRect)
        gamedisplays.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects("GAUCHE : FLECHE GAUCHE",smalltext)
        stextRect.center=((150),(400))
        hTextSurf,hTextRect=text_objects("DROITE : FLECHE DROITE" ,smalltext)
        hTextRect.center=((150),(450))
        kTextSurf, kTextRect = text_objects("SAUVEGARDEMENT AUTOMATIQUE APRES CHAQUE NIVEAU", smalltext)
        kTextRect.center = ((310), (550))
        ptextSurf,ptextRect=text_objects("P : PAUSE  ",smalltext)
        ptextRect.center=((150),(350))
        sTextSurf,sTextRect=text_objects("CONTROLS",mediumtext)
        sTextRect.center=((350),(300))
        gamedisplays.blit(sTextSurf,sTextRect)
        gamedisplays.blit(stextSurf,stextRect)
        gamedisplays.blit(hTextSurf,hTextRect)
        gamedisplays.blit(kTextSurf,kTextRect)
        gamedisplays.blit(ptextSurf,ptextRect)
        button("BACK",600,450,100,50,blue,bright_blue,"menu")
        pygame.display.update()
        clock.tick(30)



""""Pause"""

def paused():
    global pause

    while pause:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.blit(instruction_background,(0,0))
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("PAUSE",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            button("REPRENDRE",150,450,150,50,green,bright_green,"unpause")
            button("REESSAYER",350,450,150,50,blue,bright_blue,"play")
            button("MENU PRINCIPAL",550,450,200,50,red,bright_red,"menu")
            pygame.display.update()
            clock.tick(30)

""""Reprendre le jeu"""

def unpaused():
    global pause
    pause=False

"""L'arrière plan du chrono """
def countdown_background():
    font=pygame.font.SysFont(None,25)
    x=(display_width*0.45)
    y=(display_height*0.8)
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(700,0))
    gamedisplays.blit(backgroundpic,(700,200))
    gamedisplays.blit(backgroundpic,(700,400))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,500))
    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,600))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(680,100))
    gamedisplays.blit(strip,(680,0))
    gamedisplays.blit(strip,(680,200))
    gamedisplays.blit(carimg,(x,y))
    score=font.render("SCORE: 0",True,red)
    gamedisplays.blit(score,(0,30))
    button("PAUSE",650,0,150,50,blue,bright_blue,"pause")

""""Lancement d'un chrono avant que le jeu commence """

def countdown():
    countdown=True

    while countdown:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                    sys.exit()
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("3",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("2",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("1",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            gamedisplays.fill(gray)
            countdown_background()
            largetext=pygame.font.Font('freesansbold.ttf',115)
            TextSurf,TextRect=text_objects("GO!!!",largetext)
            TextRect.center=((display_width/2),(display_height/2))
            gamedisplays.blit(TextSurf,TextRect)
            pygame.display.update()
            clock.tick(1)
            game_loop()

""""Les différentes voitures """

def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load("car.jpg")
    elif obs==1:
        obs_pic=pygame.image.load("car1.jpg")
    elif obs==2:
        obs_pic=pygame.image.load("car2.jpg")
    elif obs==3:
        obs_pic=pygame.image.load("car4.jpg")
    elif obs==4:
        obs_pic=pygame.image.load("car5.jpg")
    elif obs==5:
        obs_pic=pygame.image.load("car6.jpg")
    elif obs==6:
        obs_pic=pygame.image.load("car7.jpg")
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))

""""Le score """

def score_system(passed,score):
    font=pygame.font.SysFont(None,25)
    text=font.render("Passed"+str(passed),True,black)
    score=font.render("Score"+str(score),True,red)
    gamedisplays.blit(text,(0,50))
    gamedisplays.blit(score,(0,30))

"""Police/font d'écriture"""
def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3)
    game_loop()

""""Fonction d'nterruption du jeu après l'accident"""

def crash():
    message_display("GAME OVER")


""""Définition du fond d'écran """

def background():
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,200))
    gamedisplays.blit(backgroundpic,(0,400))
    gamedisplays.blit(backgroundpic,(700,0))
    gamedisplays.blit(backgroundpic,(700,200))
    gamedisplays.blit(backgroundpic,(700,400))
    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,500))
    gamedisplays.blit(strip,(120,0))
    gamedisplays.blit(strip,(120,100))
    gamedisplays.blit(strip,(120,200))
    gamedisplays.blit(strip,(680,0))
    gamedisplays.blit(strip,(680,100))
    gamedisplays.blit(strip,(680,200))

"""Positionnement de la voiture """
def car(x,y):
    gamedisplays.blit(carimg,(x,y))


"""Coup d'envoie du jeu"""
def game_loop():
    global pause
    x=(display_width*0.45)
    y=(display_height*0.8)
    x_change=0
    obstacle_speed=9
    obs=0
    y_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=56
    obs_height=125
    passed=0
    level=1
    score=0
    y2=7
    fps=120

    bumped=False
    while not bumped:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            #Paramétrage des buttons flèche droite et flèche gauche
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change=-5
                if event.key==pygame.K_RIGHT:
                    x_change=5
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        x+=x_change
        pause=True
        gamedisplays.fill(gray)

        #Mouvement d'arrière plan
        rel_y=y2%backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic,(700,rel_y-backgroundpic.get_rect().width))


        if rel_y<800:
            gamedisplays.blit(backgroundpic,(0,rel_y))
            gamedisplays.blit(backgroundpic,(700,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y+100))
            gamedisplays.blit(yellow_strip,(400,rel_y+200))
            gamedisplays.blit(yellow_strip,(400,rel_y+300))
            gamedisplays.blit(yellow_strip,(400,rel_y+400))
            gamedisplays.blit(yellow_strip,(400,rel_y+500))
            gamedisplays.blit(yellow_strip,(400,rel_y-100))
            gamedisplays.blit(strip,(120,rel_y-200))
            gamedisplays.blit(strip,(120,rel_y+20))
            gamedisplays.blit(strip,(120,rel_y+30))
            gamedisplays.blit(strip,(680,rel_y-100))
            gamedisplays.blit(strip,(680,rel_y+20))
            gamedisplays.blit(strip,(680,rel_y+30))

        y2+=obstacle_speed


        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed,score)
        #Interruption du jeu
        if x>690-car_width or x<110:
            crash()
        if x>display_width-(car_width+110) or x<110:
            crash()
        #Le jeu continue
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(170,(display_width-170))
            obs=random.randrange(0,7)
            passed=passed+1
            score=passed*10
            # Paramétrage des niveaux du jeu
            if int(passed) % 10 == 0:
                level = level + 1
                obstacle_speed += 2
                largetext = pygame.font.Font("freesansbold.ttf", 80)
                textsurf, textrect = text_objects("LEVEL" + str(level), largetext)
                textrect.center = ((display_width / 2), (display_height / 2))
                # sauvegarde des variables niveau,score et la vitesse du voiture à nouveau
                with open("save.pkl", "wb") as pickle_file:
                    pickle.dump(passed, pickle_file)
                    pickle.dump(score, pickle_file)
                    pickle.dump(level, pickle_file)
                    pickle.dump(obstacle_speed, pickle_file)
                    print("sauvegarde réussi")
                gamedisplays.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)
        #Interruption du jeu
        if y<obs_starty+obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                crash()
        button("Pause",650,0,150,50,blue,bright_blue,"pause")
        pygame.display.update()
        clock.tick(60)

""""Chargement du jeu sauvegardé """
def game_load():
    #Vérification si le fichier existe sinon message d'erreur
    if file.exists():
        with open("save.pkl", "rb") as pickle_file:
            # On reprend la même fonction du coup d'envoi sauf que la on reccupere le niveau,score et la vitesse chargés sur save.pkl
            global pause
            x = (display_width * 0.45)
            y = (display_height * 0.8)
            x_change = 0
            obs = 0
            y_change = 0
            obs_startx = random.randrange(200, (display_width - 200))
            obs_starty = -750
            obs_width = 56
            obs_height = 125
            y2 = 7
            fps = 120
            #Réccuperation des données sauveagrdés
            passed = pickle.load(pickle_file)
            score = pickle.load(pickle_file)
            level = pickle.load(pickle_file)
            obstacle_speed = pickle.load(pickle_file)

            bumped = False
            while not bumped:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    #Paramétrage des buttons flèche droite et flèche gauche
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            x_change = -5
                        if event.key == pygame.K_RIGHT:
                            x_change = 5
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                            x_change = 0

                x += x_change
                pause = True
                gamedisplays.fill(gray)

                #Mouvement d'arrière plan
                rel_y = y2 % backgroundpic.get_rect().width
                gamedisplays.blit(backgroundpic, (0, rel_y - backgroundpic.get_rect().width))
                gamedisplays.blit(backgroundpic, (700, rel_y - backgroundpic.get_rect().width))
                if rel_y < 800:
                    gamedisplays.blit(backgroundpic, (0, rel_y))
                    gamedisplays.blit(backgroundpic, (700, rel_y))
                    gamedisplays.blit(yellow_strip, (400, rel_y))
                    gamedisplays.blit(yellow_strip, (400, rel_y + 100))
                    gamedisplays.blit(yellow_strip, (400, rel_y + 200))
                    gamedisplays.blit(yellow_strip, (400, rel_y + 300))
                    gamedisplays.blit(yellow_strip, (400, rel_y + 400))
                    gamedisplays.blit(yellow_strip, (400, rel_y + 500))
                    gamedisplays.blit(yellow_strip, (400, rel_y - 100))
                    gamedisplays.blit(strip, (120, rel_y - 200))
                    gamedisplays.blit(strip, (120, rel_y + 20))
                    gamedisplays.blit(strip, (120, rel_y + 30))
                    gamedisplays.blit(strip, (680, rel_y - 100))
                    gamedisplays.blit(strip, (680, rel_y + 20))
                    gamedisplays.blit(strip, (680, rel_y + 30))

                y2 += obstacle_speed

                obs_starty -= (obstacle_speed / 4)
                obstacle(obs_startx, obs_starty, obs)
                obs_starty += obstacle_speed
                car(x, y)
                score_system(passed, score)
                #Interruption du jeu
                if x > 690 - car_width or x < 110:
                    crash()
                if x > display_width - (car_width + 110) or x < 110:
                    crash()
                #Le jeu continue
                if obs_starty > display_height:
                    obs_starty = 0 - obs_height
                    obs_startx = random.randrange(170, (display_width - 170))
                    obs = random.randrange(0, 7)
                    passed = passed + 1
                    score = passed * 10
                    #Paramètage des niveaux du jeu
                    if int(passed) % 10 == 0:
                        level = level + 1
                        obstacle_speed += 2
                        largetext = pygame.font.Font("freesansbold.ttf", 80)
                        textsurf, textrect = text_objects("LEVEL" + str(level), largetext)
                        textrect.center = ((display_width / 2), (display_height / 2))
                        #sauvegarde des variables niveau,score et la vitesse du voiture à nouveau
                        with open("save.pkl", "wb") as pickle_file:
                            pickle.dump(passed, pickle_file)
                            pickle.dump(score, pickle_file)
                            pickle.dump(level, pickle_file)
                            pickle.dump(obstacle_speed, pickle_file)
                            print("sauvegarde reussi")
                        gamedisplays.blit(textsurf, textrect)
                        pygame.display.update()
                        time.sleep(3)
                #Interruption du jeu
                if y < obs_starty + obs_height:
                    if x > obs_startx and x < obs_startx + obs_width or x + car_width > obs_startx and x + car_width < obs_startx + obs_width:
                        crash()
                button("Pause", 650, 0, 150, 50, blue, bright_blue, "pause")
                pygame.display.update()
                clock.tick(60)
    #Message d'erreur
    else:
        largetext = pygame.font.Font("freesansbold.ttf", 20)
        textsurf, textrect = text_objects("Vous n'avez effectué aucun sauvegardement pour l'instant",largetext)
        textrect.center = ((display_width / 2), (display_height / 3.5))
        gamedisplays.blit(textsurf, textrect)


intro_loop()
game_loop()
pygame.quit()
quit()
