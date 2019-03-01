# make random path
# print area around (3x3 or 5x5?)
# move
# escape
# start

from random import randint

x = unichr(0x256C)      # all
rdl = unichr(0x2566)    # left, down, right
url = unichr(0x2569)    # left, right, up
urd = unichr(0x2560)    # up, down, right
udl = unichr(0x2563)    # up, down, left
ur = unichr(0x255A)     # up, right
ul = unichr(0x255D)     # up, left
rd = unichr(0x2554)     # down, right
dl = unichr(0x2557)     # down, left
ud = unichr(0x2551)     # up, down
rl = unichr(0x2567)     # left, right
el = unichr(0x2555)     # left
er = unichr(0x2552)     # right
eu = unichr(0x2559)     # up
ed = unichr(0x2556)     # down


print unichr(0x2520)+unichr(0x252B)
print unichr(0x2520)+unichr(0x252B)


def pathcontroller( start=(0,0), sidelength = 10):
    end = (sidelength-1, sidelength-1)
    path, squares = pathmaker(position = start, squares = [start], sidelength = sidelength,\
                              path = {start:[(start[0]-1,start[1])], end:[(end[0]+1,end[1])]})
    return path, squares, sidelength

# position is a tuple of x position ( 0 is left) and y position (0 is top)

def pathmaker(position = (0,0), squares = [(0,0)], sidelength=10,\
              path = {}):
    while len(path) < sidelength ** 2:
        dused = []
        path, newpos, squares = direction(path, position, dused, squares, sidelength)
        if newpos == 'backtrack':
            newpos = backtracker(position, squares)
        position = newpos
    return path, squares
        
# pathmaker -> control
# backtraker -> backtracks as much as necessary to continue path ->pathmaker
# direction - > moves one forward ->pathmaker

def direction(path, position, dused, squares, sidelength):
    '''
    returns updated path & squares and new position/'backtrack' if backtracking
    is necessary
    path:   a dictionary of the squares in the path as the key and the squares
            that can be accessed as the values
    position:   current square
    dused:  directions already tried
    squares:    squares that have been used as part of the path
    '''
    direct = randint(1,4)
    dmax = 4
    if position[0] == 0:
        direct = randint(1,3)
        dmax = 3
    if position[0] == sidelength-1:
        direct = randint(2,4)
        if direct == 2:
            direct = 1
        dmax = 3
    if position[1] == 0:
        direct = randint(2,4)
        dmax = 3
    if position[1] == sidelength-1:
        direct = randint(1,3)
        if direct == 3:
            direct = 4
        dmax = 3
    if position == (0,0):       # top left
        direct = randint(2,3)
        dmax = 2
    if position == (0,sidelength-1):      # bottom left
        direct = randint(1,2)
        dmax = 2
    if position == (sidelength-1, 0):     # top right
        direct = randint(3,4)
        dmax = 2
    if position == (sidelength-1, sidelength-1):        # bottom right
        direct = randint(1,2)
        if direct == 2:
            direct = 4
        dmax = 2
    if direct == 1: #up
        newpos = (position[0], position[1] - 1)
    if direct == 2: #right
        newpos = (position[0] + 1, position[1])
    if direct == 3: #down
        newpos = (position[0], position[1] + 1)
    if direct == 4: # left
        newpos = (position[0] - 1, position[1])
    if newpos in squares:
        if not direct in dused:
            dused.append(direct)
        if len(dused) == dmax:
            return path, 'backtrack', squares
        else:
            return path, 'backtrack', squares
            #return direction(path, position, dused, squares)
    else:
        if path.has_key(newpos):
            pnewpos = path[newpos] + [position]
            path[newpos] = pnewpos
        else:
            path[newpos] = [position]
        if path.has_key(position):
            ppos = path[position] + [newpos]
            path[position] = ppos
        else:
            path[position] = [newpos]
        squares.append(newpos)
        return path, newpos, squares
    
def backtracker(position, squares):
    posindex = squares.index(position)
    position = squares[posindex-1]
    return position


def mapprinter(path, sidelength):
    chars = []
    for j in range(sidelength):
        char = []
        line = ''
        for i in range(sidelength):
            square = path[(i,j)]
            if len(square) == 4:
                char.append(x)
            if len(square) == 3:
                if not (i-1,j) in square:
                    char.append(urd)
                if not (i+1,j) in square:
                    char.append(udl)
                if not (i,j-1) in square:
                    char.append(rdl)
                if not (i,j+1) in square:
                    char.append(url)
            if len(square) == 2:
                if (i,j-1) in square:
                    if (i+1,j) in square:
                        char.append(ur)
                    if (i,j+1) in square:
                        char.append(ud)
                    if (i-1,j) in square:
                        char.append(ul)
                elif (i+1,j) in square:
                    if (i,j+1) in square:
                        char.append(rd)
                    if (i-1,j) in square:
                        char.append(rl)
                else:
                    char.append(dl)
            if len(square) == 1:
                if (i,j-1) in square:
                    char.append(eu)
                if (i+1,j) in square:
                    char.append(er)
                if (i,j+1) in square:
                    char.append(ed)
                if (i-1,j) in square:
                    char.append(el)
            line = line + char[i]
        print line
        chars.append(char)
    


