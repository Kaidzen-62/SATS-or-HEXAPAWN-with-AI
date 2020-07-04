print("ViArWorld_has_RUNned")
#
import random
import time
import os
from bot_exa import R8BE
from bot_cell import RTEM
#from bot_cell import RTEM

clear = lambda: os.system('cls')

ДА_БУДЕТ_СВЕТ = True
РАБОТАЙ = True

print("ПРИВЕТ МИР!")

if (ДА_БУДЕТ_СВЕТ == True):
    print("РУССКИЙ ПОДДЕРЖИВАЕТСЯ! НО НЕНАДО ИГРАТСЯ С ЭТИМ!")

#            x,y
#WorldSize = [79,52] [64,16] - 1kb
WorldSize = [79,50]

#=worlds_arrays=================================================================
WORLD_SPACE_int1 = []
WORLD_SPACE_int2 = []
WORLD_SPACE_print = []

#RADIO SPACE
ETHER = []
for i in range(0, 19999):
    ETHER.append(0)

#         space food
Symbols = [0, 0, 0, 0, 0, 0, 0, 30, 20, 31, 9999]

#===============================================================================
#create world start position################################
for y in range(0, WorldSize[1]):
    WORLD_SPACE_int1.append([])
    WORLD_SPACE_int2.append([])
    WORLD_SPACE_print.append([])
    for x in range(0, WorldSize[0]):
        place = random.randint(0,len(Symbols)-1-3)
        WORLD_SPACE_int1[y].append(Symbols[place])
        WORLD_SPACE_int2[y].append(Symbols[place])
        WORLD_SPACE_print[y].append(' ')
############################################################

def DRAW_WORLD_SPACE():
    for y in range(0, WorldSize[1]):
        for x in range(0, WorldSize[0]):
            WORLD_SPACE_int1[y][x] = WORLD_SPACE_int2[y][x]

            if (WORLD_SPACE_int2[y][x] == 0):
                WORLD_SPACE_print[y][x] = ' '

            elif (WORLD_SPACE_int2[y][x] <= 10):
                WORLD_SPACE_print[y][x] = '.'
            elif (WORLD_SPACE_int2[y][x] <= 20):
                WORLD_SPACE_print[y][x] = 'o'

            elif (WORLD_SPACE_int2[y][x] == 30):
                WORLD_SPACE_print[y][x] = '█'

            elif (WORLD_SPACE_int2[y][x] == 31):
                WORLD_SPACE_print[y][x] = 'x'

            elif (WORLD_SPACE_int2[y][x] <= 8799):
                WORLD_SPACE_print[y][x] = '▓'

            elif (WORLD_SPACE_int2[y][x] >= 8800 and WORLD_SPACE_int2[y][x] <= 8899):
                WORLD_SPACE_print[y][x] = '☻'

            elif (WORLD_SPACE_int2[y][x] >= 9900 and WORLD_SPACE_int2[y][x] <= 9999):
                WORLD_SPACE_print[y][x] = '☺'



    for y in range(0, WorldSize[1]):
        for x in range(0, WorldSize[0]):
            print(WORLD_SPACE_print[y][x], sep=' ', end='')
        print()
    #clear()
    #time.sleep(0)

def RESTART():
    for y in range(0, WorldSize[1]):
        for x in range(0, WorldSize[0]):
            place = random.randint(0,len(Symbols)-1-3)
            WORLD_SPACE_int1[y][x] = Symbols[place]
            WORLD_SPACE_int2[y][x] = Symbols[place]

    while (len(creatures) > 0):
        creatures.pop()
    while (len(Cells) > 0):
        Cells.pop()
    #create_bots(2, 'NOPE')
    create_bots(10, 'TOP_BOT.txt')
    create_bots(10, 'LOW_BOT.txt')

    #create_cells(2, 'NOPE')
    create_cells(10, 'TOP_CELL.txt')
    create_cells(10, 'LOW_CELL.txt')



def Check(number, min, max):
    while (number >= max):
        number -= max
    while (number < min):
        number += max
    return number

def CheckAround(x, y, object): #если вокруг нет Object значит True, иначе False
    if (WORLD_SPACE[Check(y-1,0,WorldSize[1])][Check(x-1,0,WorldSize[0])] != object):
        if (WORLD_SPACE[Check(y-1,0,WorldSize[1])][Check(x,0,WorldSize[0])] != object):
            if (WORLD_SPACE[Check(y-1,0,WorldSize[1])][Check(x+1,0,WorldSize[0])] != object):

                if (WORLD_SPACE[Check(y,0,WorldSize[1])][Check(x-1,0,WorldSize[0])] != object):
                    if (WORLD_SPACE[Check(y,0,WorldSize[1])][Check(x+1,0,WorldSize[0])] != object):

                        if (WORLD_SPACE[Check(y+1,0,WorldSize[1])][Check(x-1,0,WorldSize[0])] != object):
                            if (WORLD_SPACE[Check(y+1,0,WorldSize[1])][Check(x,0,WorldSize[0])] != object):
                                if (WORLD_SPACE[Check(y+1,0,WorldSize[1])][Check(x+1,0,WorldSize[0])] != object):
                                    return True
    else:
        return False

#=CREATE_BOTS===================================================================
creatures = []
BotIndificator = [0]
def create_bots(Num, File):
    for Id in range(0, Num):
        X = 0
        Y = 0
        Fine = False

        for x in range(0, WorldSize[0]):
            for y in range(0, WorldSize[1]):
                if (WORLD_SPACE_int2[y][x] == 0):
                    X = x
                    Y = y
                    Fine = True
                    break
                    #print(X, Y, Fine)

        if (Fine):
            pram = []
            ramm = []


            for i in range(0, 19999):
                #cmd var1 var2 var3
                #pram.append([0, 0, 0, 0])
                #ramm.append([10000, 10000, 10000, 10000])
                pram.append([random.randint(0, 88), random.randint(-9999, 9999), random.randint(-9999, 9999), random.randint(-9999, 9999)])
                ramm.append([random.randint(0, 10000), random.randint(0, 10000), random.randint(0, 10000), random.randint(0, 10000)])

            #=CORRECT_BOTS_PRAM=============================================================
            #GEN============ -9999
            pram[0][0] = 19
            pram[0][1] = -1
            pram[0][2] = -1
            pram[0][3] = -9999
            #GEN============ -9998
            pram[1][0] = 19
            pram[1][1] = -1
            pram[1][2] = 0
            pram[1][3] = -9999
            #GEN============ -9997
            pram[2][0] = 1
            pram[2][1] = 1
            pram[2][2] = -1
            pram[2][3] = 1
            #GEN============ -9996
            #pram[3][0] = 63
            #pram[3][1] = -9997
            #pram[3][2] = -9999
            #pram[3][3] = -9999

            if (File != 'NOPE'):
                CD = open(File, 'r')
                NEXT = 0
                SEEK = 0
                STR = ''
                I = 0
                for line in CD:
                    #===========================================================
                    if (NEXT == 0 and line == 'PRAM' + '\n'):
                        NEXT = 1
                        continue

                    #===========================================================
                    if (NEXT == 6):
                        if (line == 'RAMM' + '\n'):
                            I = 0
                            NEXT = 7
                            continue
                        else:
                            NEXT = 1

                    #===========================================================
                    if (NEXT == 1):
                        SEEK = 5
                        NEXT = 2
                        while (NEXT == 2):
                            if (line[SEEK] == ','):
                                NEXT = 3
                                pram[I][0] = int(STR)
                                STR = ''
                            else:
                                STR += line[SEEK]

                            SEEK += 1

                        while (NEXT == 3):
                            if (line[SEEK] == ','):
                                NEXT = 4
                                pram[I][1] = int(STR)
                                STR = ''
                            else:
                                STR += line[SEEK]

                            SEEK += 1

                        while (NEXT == 4):
                            if (line[SEEK] == ','):
                                NEXT = 5
                                pram[I][2] = int(STR)
                                STR = ''
                            else:
                                STR += line[SEEK]

                            SEEK += 1

                        while (NEXT == 5):
                            if (line[SEEK] == '.'):
                                NEXT = 6
                                pram[I][3] = int(STR)
                                STR = ''
                            else:
                                STR += line[SEEK]

                            SEEK += 1
                        continue
                    #===========================================================
                    if (NEXT == 7):
                        if (line == 'FEND'):
                            break
                        else:
                            NEXT = 8
                    #===========================================================
                    if (NEXT == 8):
                        SEEK = 0
                        NEXT = 9
                        while (NEXT == 9):
                            if (line[SEEK] == ','):
                                NEXT = 10
                                ramm[I][0] = int(STR)
                                STR = ''
                            else:
                                STR += line[SEEK]

                            SEEK += 1

                        while (NEXT == 10):
                            if (line[SEEK] == ','):
                                NEXT = 11
                                ramm[I][1] = int(STR)
                                STR = ''
                            else:
                                STR += line[SEEK]

                            SEEK += 1

                        while (NEXT == 11):
                            if (line[SEEK] == ','):
                                NEXT = 12
                                ramm[I][2] = int(STR)
                                STR = ''
                            else:
                                STR += line[SEEK]

                            SEEK += 1

                        while (NEXT == 12):
                            if (line[SEEK] == '.'):
                                NEXT = 7
                                ramm[I][3] = int(STR)
                                STR = ''
                            else:
                                STR += line[SEEK]

                            SEEK += 1
                        continue
                    #===========================================================
                CD.close()

            #INIT( X, Y, ID, PC, PRAM, RAMM, CMhangry, MutationKa, MutationChance)
            creatures.append(R8BE(X, Y, BotIndificator[0], (-9999), pram, ramm, 1, 0, 7000))
            WORLD_SPACE_int2[Y][X] = 9999
            BotIndificator[0] += 1
#=CREATE_CELLS==================================================================
Cells = []
CellIndificator = [0]
def create_cells(Num, File):
    for Id in range(0, Num):
        X = 0
        Y = 0
        Fine = False

        for x in range(WorldSize[0] -1, -1, -1):
            for y in range(WorldSize[1] -1, -1, -1):
                if (WORLD_SPACE_int2[y][x] == 0):
                    X = x
                    Y = y
                    Fine = True
                    break
                    #print(X, Y, Fine)

        if (Fine):
            WORLD_SPACE_int1[Y][X] = 8899
            pram = []
            PRAM_LEN = 2**12
            for i in range(0, PRAM_LEN):
                pram.append(random.randint(0, PRAM_LEN-1))

            #=CORRECT_CELLS_PRAM================================================
            pram[0] = 35
            pram[1] = 36

            #INIT(self, x, y, id, PRAM, CMhangry, MutationKa, MutationChance, RED, BLU)
            RED = random.randint(0, len(pram)-1)
            BLU = random.randint(0, len(pram)-1)

            while (BLU == RED):
                BLU = random.randint(0, 255)

            if (File != 'NOPE'):
                CD = open(File, 'r')
                NEXT = 0
                SEEK = 0
                STR = ''
                I = 0
                for line in CD:
                    if (line[0] != '!'):
                        pram[I] = int(str(line[0]) + str(line[1]) + str(line[2]) + str(line[3]) + str(line[4]))
                        I += 1

                CD.close()
            Cells.append(RTEM(X, Y, CellIndificator, pram, 1, 0, 7000, RED, BLU))
            WORLD_SPACE_int2[Y][X] = 8899
            CellIndificator[0] += 1
#SOME_FUNCTIONS_FOR_WIRLD_WORK==================================================
def CheckX(x):
    return Check(x, 0, WorldSize[0])

def CheckY(y):
    return Check(y, 0, WorldSize[1])

#=WORLD_RULES===================================================================
def Rules():
    #bots################################################################################################
    for Id in range(0, len(creatures)):
        Id = Check(Id, 0, len(creatures))
        Xb = creatures[Id].x
        Yb = creatures[Id].y
        WORLD_SPACE_int2[Yb][Xb] = 9999

        visionSmall = []
        visionFull = []
        #make vision arrays
        #visionSmall
        for y in range(-1, 2, 1):
            visionSmall.append([])
            for x in range(-1, 2, 1):
                visionSmall[y + 1].append( WORLD_SPACE_int1[CheckY(Yb+y)][CheckX(Xb+x)] )

        #visionFull
        for y in range(-2, 3, 1):
            for x in range(-2, 3, 1):
                visionFull.append( WORLD_SPACE_int1[CheckY(Yb+y)][CheckX(Xb+x)] )

        #TIC BOT: visionSmall, visionFull, ETHER
        #BotOP = Bot Out Put
        BotOP = creatures[Id].tic(visionSmall, visionFull, ETHER)
        #OUT PUT: MOVE_X, MOVE_Y, REPL_X, REPL_Y, REPL_PC, REPL_STATE, DOAC_X, DOAC_Y, DOAC_C, RDIS_HZ, RDOS_VAL
        #            0       1      2       3        4         5         6       7       8        9       10

        #IF BOT IS NOT DEAD: CONTINUE
        if (not(BotOP[5] == -1)):
            #move bot
            #move out
            if (WORLD_SPACE_int2[ CheckY(Yb + BotOP[1]) ][ CheckX(Xb + BotOP[0]) ] <= 20 or WORLD_SPACE_int2[ CheckY(Yb + BotOP[1]) ][ CheckX(Xb + BotOP[0]) ] == 31):
                WORLD_SPACE_int2[Yb][Xb] = 0

                creatures[Id].x = CheckX(creatures[Id].x + BotOP[0])
                creatures[Id].y = CheckY(creatures[Id].y + BotOP[1])

                Xb = creatures[Id].x
                Yb = creatures[Id].y

                if (WORLD_SPACE_int2[Yb][Xb] <= 20):
                    creatures[Id].hangry += WORLD_SPACE_int2[Yb][Xb]
                elif (WORLD_SPACE_int2[Yb][Xb] == 31):
                    creatures[Id].hangry = -31
                #drow bot on map
                WORLD_SPACE_int2[Yb][Xb] = 9999

            #RADIO!!!
            ETHER[BotOP[9]] = BotOP[10]

            #DO ACTION!!!
            ACT = BotOP[8]
            BLOCKS_IDS = 31
            #SPACE
            if (WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])] == 0):
                if (creatures[Id].inventory == 0):
                    #nothing
                    pass
                else:
                    if (ACT > 0):
                        #set block
                        WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])] = creatures[Id].inventory
                        creatures[Id].inventory = 0
            #BLOCK
            elif (WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])] <= BLOCKS_IDS):
                if (creatures[Id].inventory == 0):
                    if (ACT > 0):
                        #ACTion on block
                        pass
                    elif (ACT < 0):
                        #grab block
                        creatures[Id].inventory = WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])]
                        WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])] = 0
                else:
                    if (ACT > 0):
                        #ACTion on block
                        pass
                    elif (ACT < 0):
                        #SWAP BLOCKS
                        SWP = creatures[Id].inventory
                        creatures[Id].inventory = WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])]
                        WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])] = SWP

            #CELL
            elif (WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])] >= 8800 and WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])] <= 8899):
                for i in range(0, len(Cells)):
                    if (Cells[i].x == CheckX(Xb + BotOP[6]) and Cells[i].y == CheckX(Yb + BotOP[7])):
                        if (ACT > 0):
                            Cells[i].healPoint += 30
                            #Cells[i].BLU_flag = True
                            creatures[Id].hangry-= 30
                        elif (ACT < 0):
                            Cells[i].healPoint -= 30
                            Cells[i].RED_flag = True
                            creatures[Id].hangry += 30

            #BOT
            elif (WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])] >= 9900 and WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])] <= 9999):
                for i in range(0, len(creatures)):
                    if (creatures[i].x == CheckX(Xb + BotOP[6]) and creatures[i].y == CheckY(Yb + BotOP[7])):
                        if (ACT > 0):
                            creatures[i].hangry += 30
                            creatures[Id].hangry -= 30
                        elif (ACT < 0):
                            creatures[i].hangry -= 30
                            creatures[Id].hangry += 30


            if (ACT == 666):
                WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])] += 1
                WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])] = Check(WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])], 0, 10000)
            elif (ACT == -666):
                WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])] -= 1
                WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])] = Check(WORLD_SPACE_int2[CheckY(Yb + BotOP[7])][CheckX(Xb + BotOP[6])], 0, 10000)


            #REPLICATION
            if (BotOP[5] == 1 and len(creatures) <= (WorldSize[0] * WorldSize[1]) ):
                if (WORLD_SPACE_int2[ CheckY(creatures[Id].y + BotOP[3]) ][ CheckX(creatures[Id].x + BotOP[2])] <= 20 or WORLD_SPACE_int2[ CheckY(creatures[Id].y + BotOP[3]) ][ CheckX(creatures[Id].x + BotOP[2])] == 31):

                    EatFBorn = WORLD_SPACE_int2[CheckY(creatures[Id].y + BotOP[3])][ CheckX(creatures[Id].x + BotOP[2]) ]
                    if (WORLD_SPACE_int2[CheckY(creatures[Id].y + BotOP[3])][ CheckX(creatures[Id].x + BotOP[2]) ] == 31):
                        EatFBorn = -31

                    BotIndificator[0] += 1
                    variationsHangryCof = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4]
                    HangryCof = random.randint(1, 10) * variationsHangryCof[random.randint(0, len(variationsHangryCof)-1)]

                    #INIT( X, Y, ID, PRAM, RAMM, PC, CMhangry, MutationKa, MutationChance)
                    creatures.append(R8BE( CheckX(creatures[Id].x + BotOP[2]), CheckY(creatures[Id].y + BotOP[3]), BotIndificator[0], BotOP[4], creatures[Id].pram, creatures[Id].ramm, HangryCof, 1, 2500))

                    creatures[Id].hangry -= 101
                    creatures[len(creatures)-1].hangry = 100
                    creatures[len(creatures)-1].hangry += EatFBorn

                    WORLD_SPACE_int2[CheckY(creatures[Id].y + BotOP[3])][ CheckX(creatures[Id].x + BotOP[2]) ] = 9999
                    break
                else:
                    creatures[Id].hangry -= 50

        else:
            if (creatures[Id].hangry >= 20):
                WORLD_SPACE_int2[Yb][Xb] = 20
            elif (creatures[Id].hangry < 20):
                WORLD_SPACE_int2[Yb][Xb] = creatures[Id].hangry
            WORLD_SPACE_int2[Yb][Xb] = Check(WORLD_SPACE_int2[Yb][Xb], 0, 20)
            creatures.pop(Id)
            Id -= 1
            continue
    #bots-end#########################################################################################
    #cells############################################################################################
    for Id in range(0, len(Cells)):
        Id = Check(Id, 0, len(Cells))
        Xc = Cells[Id].x
        Yc = Cells[Id].y
        WORLD_SPACE_int2[Yc][Xc] = 8899

        visionSmall = []
        #visionSmall
        for y in range(-1, 2, 1):
            visionSmall.append([])
            for x in range(-1, 2, 1):
                visionSmall[y + 1].append( WORLD_SPACE_int1[CheckY(Yc+y)][CheckX(Xc+x)] )

        #TIC CELL (visionSmall, RED_flag, RED_pmtr, BLU_flag, BLU_pmtr)
        #CellOP = CELL OUT PUT
        CellOP = Cells[Id].tic(visionSmall)
        #OUT PUT: MOVE_X, MOVE_Y, REPL_X, REPL_Y, REPL_STATE, DOAC_X, DOAC_Y, DOAC_C
        #            0       1      2       3        4         5         6       7

        #IF BOT IS NOT DEAD: CONTINUE
        if (not(CellOP[4] == -1)):
            #move cell
            if (WORLD_SPACE_int2[ CheckY(Yc + CellOP[1]) ][ CheckX(Xc + CellOP[0]) ] <= 20 or WORLD_SPACE_int2[ CheckY(Yc + CellOP[1]) ][ CheckX(Xc + CellOP[0]) ] == 31):
                WORLD_SPACE_int2[Yc][Xc] = 0

                Cells[Id].x = CheckX(Cells[Id].x + CellOP[0])
                Cells[Id].y = CheckY(Cells[Id].y + CellOP[1])

                Xc = Cells[Id].x
                Yc = Cells[Id].y

                if (WORLD_SPACE_int2[Yc][Xc] <= 20):
                    Cells[Id].healPoint += WORLD_SPACE_int2[Yc][Xc]
                elif (WORLD_SPACE_int2[Yc][Xc] == 31):
                    Cells[Id].healPoint = -31
                #drow bot on map
                WORLD_SPACE_int2[Yc][Xc] = 8899

            #DO ACTION!!!
            ACT = CellOP[7]
            BLOCKS_IDS = 30
            #CELL
            if (WORLD_SPACE_int2[CheckY(Yc + CellOP[6])][CheckX(Xc + CellOP[5])] >= 8800 and WORLD_SPACE_int2[CheckY(Yc + CellOP[6])][CheckX(Xc + CellOP[5])] <= 8899):
                for i in range(0, len(Cells)):
                    if (Cells[i].x == CheckX(Xc + CellOP[5]) and Cells[i].y == CheckY(Yc + CellOP[6])):
                        if (ACT > 0):
                            Cells[i].healPoint += 10
                            #Cells[i].BLU_flag = True
                            Cells[Id].healPoint-= 10
                        elif (ACT < 0):
                            Cells[i].healPoint -= 10
                            Cells[i].RED_flag = True
                            Cells[Id].healPoint += 10
            #BOT
            elif (WORLD_SPACE_int2[CheckY(Yc + CellOP[6])][CheckX(Xc + CellOP[5])] >= 9900 and WORLD_SPACE_int2[CheckY(Yc + CellOP[6])][CheckX(Xc + CellOP[5])] <= 9999):
                for i in range(0, len(creatures)):
                    if (creatures[i].x == CheckX(Xc + CellOP[5]) and creatures[i].y == CheckY(Yc + CellOP[6])):
                        if (ACT > 0):
                            creatures[i].hangry += 10
                            Cells[Id].healPoint -= 10
                        elif (ACT < 0):
                            creatures[i].hangry -= 50 #-50
                            Cells[Id].healPoint += 50 #+50



            #REPLICATION
            if (CellOP[4] == 1 and len(Cells) <= (WorldSize[0] * WorldSize[1]) and (Cells[Id].healPoint) > 50):
                if (WORLD_SPACE_int2[ CheckY(Cells[Id].y + CellOP[3]) ][ CheckX(Cells[Id].x + CellOP[2])] <= 20 or WORLD_SPACE_int2[ CheckY(Cells[Id].y + CellOP[3]) ][ CheckX(Cells[Id].x + CellOP[2])] == 31):

                    EatFBorn = WORLD_SPACE_int2[CheckY(Cells[Id].y + CellOP[3])][ CheckX(Cells[Id].x + CellOP[2]) ]

                    if (WORLD_SPACE_int2[CheckY(Cells[Id].y + CellOP[3])][ CheckX(Cells[Id].x + CellOP[2]) ] == 31):
                        EatFBorn = -31

                    CellIndificator[0] += 1
                    variationsHangryCof = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4]
                    HangryCof = random.randint(1, 2) * variationsHangryCof[random.randint(0, len(variationsHangryCof)-1)]

                    #__init__(self, x, y, id, PRAM, CMhangry, MutationKa, MutationChance, RED, BLU):
                    Cells.append(RTEM( CheckX(Cells[Id].x + CellOP[2]), CheckY(Cells[Id].y + CellOP[3]), CellIndificator[0], Cells[Id].pram, HangryCof, 1, 3500, Cells[Id].RED, Cells[Id].BLU))

                    Cells[Id].healPoint -= 80
                    Cells[len(Cells)-1].healPoint += EatFBorn

                    WORLD_SPACE_int2[CheckY(Cells[Id].y + CellOP[3])][ CheckX(Cells[Id].x + CellOP[2]) ] = 8899
                    break
                else:
                    Cells[Id].healPoint -= 10

        else:
            WORLD_SPACE_int2[Yc][Xc] = Check(Cells[Id].healPoint, 0, 20)
            Cells.pop(Id)
            Id -= 1
            continue
    #cells-end########################################################################################
    #cellular#########################################################################################
    for y in range(0, WorldSize[1]):
        for x in range(0, WorldSize[0]):
            ##########################################################################################
            Eat_cof = random.randint(0, 200)

            if (WORLD_SPACE_int2[y][x] == 0): ##TREE
                if (random.randint(0,10001) <= Eat_cof):
                    WORLD_SPACE_int2[y][x] = random.randint(0, 10)
                    break
            elif (WORLD_SPACE_int2[y][x] <= 10): ##TREE
                if (random.randint(0,10001) <= Eat_cof):
                    WORLD_SPACE_int2[y][x] = random.randint(10, 20)
                    break
                break
            elif (WORLD_SPACE_int2[y][x] <= 20):
                if (random.randint(0,10001) <= Eat_cof + random.randint(-5, 20)):
                    WORLD_SPACE_int2[y][x] = 31
                    break
                break
            elif (WORLD_SPACE_int2[y][x] == 31):
                if (random.randint(0,10001) <= Eat_cof + random.randint(-5, 20)):
                    WORLD_SPACE_int2[y][x] = 0
                    break
            ##########################################################################################

    #cellular-end#####################################################################################

def CHECK_LIDERS(File):
    TOP = open(File)
    a = TOP.read(1)
    score = int( TOP.read(1) + TOP.read(1) + TOP.read(1) + TOP.read(1) + TOP.read(1) + TOP.read(1) + TOP.read(1) + TOP.read(1) + TOP.read(1) + TOP.read(1))
    TOP.close()

    TEST = 0
    ID = 0
    if (File == 'TOP_BOT.txt'):
        for Id in range(0, len(creatures)):
            if (creatures[Id].age > TEST):
                TEST = creatures[Id].age
                ID = Id
    elif (File == 'LOW_BOT.txt'):
        for Id in range(0, len(creatures)):
            if (creatures[Id].age > TEST and creatures[Id].age <= 500):
                score = 0
                TEST = creatures[Id].age
                ID = Check(Id, 0, len(creatures))

    if (creatures[ID].age > score):
        TOP = open(File, 'w')

        if (File == 'TOP_BOT.txt'):
            TOP.write('!' + str(creatures[ID].age) + '          ' + str(creatures[ID].hangry) + ' ' + str(creatures[ID].healPoint) + '\n')
        elif (File == 'LOW_BOT.txt'):
            TOP.write('!' + '0000000000 ' + str(creatures[ID].hangry) + ' ' + str(creatures[ID].healPoint) + '\n')

        TOP.write('PRAM' + '\n')
        for i in range(0, 19999):
            code = ''
            if (creatures[ID].pram[i][0] == 0):
                code = 'NOPE ' + '0'
            elif (creatures[ID].pram[i][0] <= 4):
                code = 'MOVE ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 8):
                code = 'SEEK ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 10):
                code = 'SEEG ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 18):
                code = 'DOAC ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 26):
                code = 'REPL ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 28):
                code = 'RDIS ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 32):
                code = 'RDOS ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 34):
                code = 'STRV ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 36):
                code = 'LDRI ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 38):
                code = 'LDRX ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 40):
                code = 'LDRY ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 42):
                code = 'LDRC ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 46):
                code = 'ADDI ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 50):
                code = 'SUBI ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 54):
                code = 'MULI ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 58):
                code = 'DIVI ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 62):
                code = 'MODI ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 64):
                code = 'JUMP ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 66):
                code = 'JALZ ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 68):
                code = 'JAGZ ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 70):
                code = 'JAEZ ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 76):
                code = 'JALA ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 82):
                code = 'JAGA ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 88):
                code = 'JAEA ' + str(creatures[ID].pram[i][0])
            elif (creatures[ID].pram[i][0] <= 91):
                code = 'SWIZ ' + str(creatures[ID].pram[i][0])

            TOP.write(code + ',' + str(creatures[ID].pram[i][1]) + ',' + str(creatures[ID].pram[i][2]) + ',' + str(creatures[ID].pram[i][3]) + '.' + '\n')

        TOP.write('RAMM' + '\n')
        for i in range(0, 19999):
            TOP.write( str(creatures[ID].ramm[i][0]) + ',' + str(creatures[ID].ramm[i][1]) + ',' + str(creatures[ID].ramm[i][2]) + ',' + str(creatures[ID].ramm[i][3]) + '.' + '\n')

        TOP.write('FEND')
        TOP.close()

def CHECK_LIDERS_CELLS(File):
    TOP = open(File)
    a = TOP.read(1)
    score = int( TOP.read(1) + TOP.read(1) + TOP.read(1) + TOP.read(1) + TOP.read(1) + TOP.read(1) + TOP.read(1) + TOP.read(1) + TOP.read(1) + TOP.read(1))
    TOP.close()

    TEST = 0
    ID = 0
    if (File == 'TOP_CELL.txt'):
        for Id in range(0, len(Cells)):
            if (Cells[Id].age > TEST):
                TEST = Cells[Id].age
                ID = Id
    elif (File == 'LOW_CELL.txt'):
        for Id in range(0, len(Cells)):
            if (Cells[Id].age > TEST and Cells[Id].age <= 500):
                score = 0
                TEST = Cells[Id].age
                ID = Check(Id, 0, len(Cells))

    if (Cells[ID].age > score):
        TOP = open(File, 'w')

        if (File == 'TOP_CELL.txt'):
            TOP.write('!' + str(Cells[ID].age) + '            ' + str(Cells[ID].healPoint) + '\n')

        elif (File == 'LOW_CELL.txt'):
            TOP.write('!' + '000000000000  ' + str(Cells[ID].healPoint) + '\n')

        for pc in range(0, len(Cells[ID].pram)):
            TOP.write(str(Cells[ID].pram[pc]) + '          ' + '\n')

        TOP.close()

def SAVE_LOAD_BOTS(DO):
    if (DO == 'SAVE'):
        CD = open('BOTS.txt', 'w')
        for Id in range(0, len(creatures)):
            CD.write('BOT number ' + str(Id) + '\n')#pram begin
            for j in range(0, 19999):
                CD.write(str(creatures[Id].pram[j][0]) + '             ' + '\n')
                CD.write(str(creatures[Id].pram[j][1]) + '            ' +  '\n')
                CD.write(str(creatures[Id].pram[j][2]) + '            ' +  '\n')
                CD.write(str(creatures[Id].pram[j][3]) + '            ' +  '\n')
            CD.write('RE\n')#pram end
            for j in range(0, 19999): #ramm begin
                CD.write(str(creatures[Id].ramm[j][0]) + '            ' +  '\n')
                CD.write(str(creatures[Id].ramm[j][1]) + '            ' +  '\n')
                CD.write(str(creatures[Id].ramm[j][2]) + '            ' +  '\n')
                CD.write(str(creatures[Id].ramm[j][3]) + '            ' +  '\n')
            CD.write('END\n')#ramm end
        CD.close()

    elif (DO == 'LOAD'):
        CD = open('BOTS.txt', 'r')

        BotIndificator[0] = 0
        pram = []
        ramm = []

        for i in range(0, 19999):
            pram.append([0, 0, 0, 0])
            ramm.append([0, 0, 0, 0])

        NEXT = -1
        next_i = 0
        for line in CD:
            if (line[0] == 'B' and NEXT == -1):
                NEXT = 0
                continue

            if (NEXT == 0):
                pram[next_i][0] = int(str(line[0]) + str(line[1]) + str(line[2]) + str(line[3]) + str(line[4]))
                NEXT = 1

            if (NEXT == 1):
                pram[next_i][1] = int(str(line[0]) + str(line[1]) + str(line[2]) + str(line[3]) + str(line[4]))
                NEXT = 2

            if (NEXT == 2):
                pram[next_i][2] = int(str(line[0]) + str(line[1]) + str(line[2]) + str(line[3]) + str(line[4]))
                NEXT = 3

            if (NEXT == 3):
                pram[next_i][3] = int(str(line[0]) + str(line[1]) + str(line[2]) + str(line[3]) + str(line[4]))
                NEXT = 0
                next_i += 1
                if (next_i == 19998):
                    next_i = 0
                    NEXT = 4

            if (NEXT == 4 and line[0] == 'R'):
                NEXT = 5
                continue

            #================================
            if (NEXT == 5):
                ramm[next_i][0] = int(str(line[0]) + str(line[1]) + str(line[2]) + str(line[3]) + str(line[4]))
                NEXT = 6

            if (NEXT == 5):
                ramm[next_i][1] = int(str(line[0]) + str(line[1]) + str(line[2]) + str(line[3]) + str(line[4]))
                NEXT = 6

            if (NEXT == 6):
                ramm[next_i][2] = int(str(line[0]) + str(line[1]) + str(line[2]) + str(line[3]) + str(line[4]))
                NEXT = 7

            if (NEXT == 7):
                ramm[next_i][3] = int(str(line[0]) + str(line[1]) + str(line[2]) + str(line[3]) + str(line[4]))
                NEXT = 5
                next_i += 1
                if (next_i == 19998):
                    next_i = 0
                    NEXT = 8

            if (NEXT == 8 and line[0] == 'E'):
                X = 0
                Y = 0
                Fine = False

                for y in range(0, WorldSize[1]):
                    for x in range(0, WorldSize[0]):
                        if (WORLD_SPACE_int1[y][x] == 0):
                            X = x
                            Y = y
                            Fine = True
                            break

                if (Fine):
                    creatures.append(R8BE(X, Y, BotIndificator[0], (-9999), pram, ramm, 1, 0, 2500))
                    BotIndificator[0] += 1
                    NEXT = -1
                    next_i = 0

        CD.close()
#===============================================================================
#create_bots(100, 'NOPE')
create_bots(20, 'TOP_BOT.txt')
create_bots(20, 'LOW_BOT.txt')
#SAVE_LOAD_BOTS('LOAD')

#create_cells(100, 'NOPE')
create_cells(100, 'TOP_CELL.txt')
create_cells(100, 'LOW_CELL.txt')
#===============================================================================
WORLD_TIME = 1
DAY = False
DAYcount = 0
World_N = 1
while(РАБОТАЙ):
    #code################################
    if (WORLD_TIME % 100 == 0):
        DAY = not(DAY)
        if DAY:
            DAYcount += 1
    #####################################
    Rules()
#
#
    clear()
    DRAW_WORLD_SPACE()
    #data#################################
    print('--------------------------------------------------------------------------------')
    #print('DAY IS:',DAY)
    #print('DAY COUNT:',DAYcount)
    print('WORLD TIME:',WORLD_TIME)
    print('World N:',World_N)
    print('N bots:',len(creatures))
    print('N Cells:',len(Cells))
    ######################################
    #time.sleep(1)
#
    if (WORLD_TIME % 256 == 0):
        if (len(creatures) > 0):
            CHECK_LIDERS('TOP_BOT.txt')
            CHECK_LIDERS('LOW_BOT.txt')

        if (len(Cells) > 0):
            CHECK_LIDERS_CELLS('TOP_CELL.txt')
            CHECK_LIDERS_CELLS('LOW_CELL.txt')

    if (WORLD_TIME % 200000 == 0):
        if (len(creatures) > 0):
            SAVE_LOAD_BOTS('SAVE')

    if (len(creatures) == 0 and len(Cells) == 0):
        RESTART()
        if (len(creatures) > 0):
            CHECK_LIDERS('TOP_BOT.txt')
            CHECK_LIDERS('LOW_BOT.txt')

        if (len(Cells) > 0):
            CHECK_LIDERS_CELLS('TOP_CELL.txt')
            CHECK_LIDERS_CELLS('LOW_CELL.txt')
        World_N += 1
        WORLD_TIME = 1
    #
    #
    WORLD_TIME += 1
    if (WORLD_TIME >= 2**20):
        if (len(creatures) > 0):
            CHECK_LIDERS('TOP_BOT.txt')
            CHECK_LIDERS('LOW_BOT.txt')
            SAVE_LOAD_BOTS('SAVE')

        if (len(Cells) > 0):
            CHECK_LIDERS_CELLS('TOP_CELL.txt')
            CHECK_LIDERS_CELLS('LOW_CELL.txt')
        РАБОТАЙ = False

#улучшить мозг ботов (переместить ram в prom область)
#добавить в мир клетосный автомат WIREWORLD
