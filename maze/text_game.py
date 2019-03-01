
# items in locations
itemsstartroom = {'bed':'It is an exceptionally lumpy bed. It is probably bes'+\
                  't to not look further.',\
                  'window':'The window is too dirty to see much out of, but y'+\
                  'ou appear to be in a small town.',\
                  'door':['It is unlocked.',None,['exit']]}

# 2nd items in locations
2itemsstartroom = {'bed':['You should not have looked further. You see some vo'+\
                   'mit from hopefully the night before. You are revolted and'+\
                   'vomit again.',['heal-010']]}

def actionparser(action, stats, items, itemloc):
    for i in range(len(action)):
        a = action[i]
        ref = a[:4]
        amount = (a[4:])
        if ref == 'heal':
            stats[0] = min(100, stats[0] + int(amount))
            print 'Your health is now at ',stats[0]
            if stats[0] <= 0:
                print 'You have died'
                endgame()   # still need to make
        if ref == 'ener':
            stats[1] = min(100, stats[0] + int(amount))
            print 'Your energy is now at ',stats[1]
            if stats[1] <= 0:
                print 'You faint from lack of energy'
                nap()           # SNTM Nap requires something probably - ???
        if ref == 'mone':
            stats[2] = stats[2] + int(amount)
            print 'You now have ',stats[2],'gold.'
        if ref == 'item':
            if amount[0] == '-' and item in items:
                
                
            

#moves

moves = {'look':look, 'look again':look_again}

def look(item, itemloc, items):
    action = [None]
    if item in (itemshave or itemloc):
        if item in items:
            z = items[item]
        if item in itemloc:
            z = itemloc[item]
        if type(z) == list:
            mes = z[0]
            action = z[1]
        else: mes = z
        print z
    if item not in items:
        print 'I do not understand'
    return action

def look_again(item, 2itemloc, 2items):
    action = [None]
    if item in (2items or 2itemloc):
        if item in 2items:
            z = 2items[item]
        if item in 2itemloc:
            z = 2itemloc[item]
        print 2items[item]

def opn(item, itemloc, items):
    if item in itemloc:
        if len(itemloc[item]) > 2:
            #something happens
        else:
            print 'This cannot be opened'
    if item in items:
        if len(items[item]) > 2:
            #something happens
        else:
            print 'This cannot be opened'

#locations
def startroom(items, stats, 2items):
    exited = False
    while not exited:
        move = raw_input('')
        

def rungame():
    stats = [100,50,0]   # health(heal/100), energy(ener/100), money(mone)
    items ={'self':'You are a bit scruffy looking, but all in all a pret'+\
            'ty decent person. Sure you have your flaws, but who doesn\'t?',\
            'shirt':'It is a basic shirt, very well worn.',\
            'pants':'They are pants. That is all',\
            'shoes':'They appear to fit more or less.'}
    2items = {'self':'It is wise to remember the proverb, "If you spend a'+\
              'll your time looking inwards, you won\'t see the guy about'+\
              ' to punch you in the face".'}
    print 'You wake in an uncomfortable bed, with a pounding headache and no '+\
          'recollection of how you got here. Perhaps you should lay off the '+\
          'mead in future.'
    startroom(items, stats, 2items)
    
