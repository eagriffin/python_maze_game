from maze import pathcontroller, mapprinter
import pygame
import time

start = (0,0)
path, squares, sl = pathcontroller(start = start, sidelength = 20)
mapprinter(path, sl)

prevpos = (start[0]-1,start[1])
position = start


def rungame(position, prevpos):
    pygame.init()

    screen = pygame.display.set_mode((360,360))

    clock = pygame.time.Clock()

    bkgd = pygame.image.load('f.png')
    f = pygame.image.load('f.png')
    r = pygame.image.load('r.png')
    l = pygame.image.load('l.png')
    rl = pygame.image.load('rl.png')
    fr = pygame.image.load('fr.png')
    fl = pygame.image.load('fl.png')
    frl = pygame.image.load('frl.png')
    no = pygame.image.load('no.png')

    wallmes = pygame.image.load('wallmessage.png')
    entermes = pygame.image.load('entermes.png')
    nomes = pygame.image.load('nomes.png')

    
    screen.blit(bkgd, (0,0))
    change = True
    direction = 2
    dirs = [2]
    mestype = entermes
    while True:
        clock.tick(40)

        if change:
            change = False
            if position[0] != prevpos[0]:
                if position[0] == prevpos[0]+1:
                    direction = 2
                else:
                    direction = 4
            else:
                if position[1] == prevpos[1]+1:
                    direction = 3
                else:
                    direction = 1

            options = path[position]

            print options, position, prevpos
            dirs = []
            for i in range(len(options)):
                if options[i][0] != position[0]:
                    if options[i][0] == position[0]+1:
                        dirs.append(2)
                    else:
                        dirs.append(4)
                else:
                    if options[i][1] == position[1]+1:
                        dirs.append(3)
                    else:
                        dirs.append(1)
            print dirs
            if len(dirs) == 4:
                bkgd = frl
            if len(dirs) == 3:
                if direction in dirs:
                    if direction+1 in dirs:
                        bkgd = fr
                    else:
                        bkgd = fl
                else:
                    bkgd = rl
            if len(dirs) == 2:
                if direction in dirs:
                    bkgd = f
                if direction+1 in dirs:
                    bkgd = r
                if direction-1 in dirs or direction+3 in dirs:
                    bkgd = l
            if len(dirs) == 1:
                bkgd = no

            screen.blit(bkgd, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
                return None
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                direct = direction+2
                change = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                direct = direction
                change = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                direct = direction+1
                change = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                direct = direction+3
                change = True

            if change:
                mestype = nomes
                if position == start and (start[0]-1,start[1]) in options:
                    options.remove((start[0]-1,start[1]))
                    mestype = entermes
                print direct

                if direct > 4:
                    direct += -4
    
                if not direct in dirs:
                    mestype = wallmes
                    print 'You cannot walk through walls.'
                    break
                
                prevpos = position
                print position, prevpos
                    
                if True:
                    if direct == 1:
                        position = (position[0], position[1]-1)
                    if direct == 2:
                        position = (position[0]+1, position[1])
                    if direct == 3:
                        position = (position[0], position[1]+1)
                    if direct == 4:
                        position = (position[0]-1, position[1])
                if position == (sl,sl-1):
                    win_game()
                    return None
        screen.blit(mestype, (0,300))
        pygame.display.flip()


def exit_game():
    pygame.quit()
    return None

def win_game():
    print 'you win'
    pygame.quit()
    return None





rungame(position, prevpos)
