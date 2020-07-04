import random

class RTEM():
    def __init__(self, x, y, id, PRAM, CMhangry, MutationKa, MutationChance, RED, BLU):
        self.id = id
        self.x = x
        self.y = y
        #programm memory
        self.pram = PRAM
        self.MutationKa = MutationKa
        #=======================================================================
        self.age = 0
        self.healPoint = 300
        self.CMhangry = CMhangry
        self.pc = 0

        self.stack = 0
        self.RED_flag = False
        self.RED_pmtr = 0
        self.RED = RED
        self.BLU_flag = False
        self.BLU_pmtr = 0
        self.BLU = BLU

        #РЕГИСТРЫ ВХОДА/ВЫХОДЯ И ДЕЙСТВИЯ
        #move IN
        self.MOVE_X = 0
        self.MOVE_Y = 0

        #REPL
        self.REPL_X = 0
        self.REPL_Y = 0
        self.REPL_STATE = 0 #0 - NOPE; 1 - REPL EN; -1 - DEATH

        #DOAC
        self.DOAC_X = 0
        self.DOAC_Y = 0
        self.DOAC_C = 0 #positive action and negative action and 0 is NOPE

        def Check(number, min, max):
            while (number >= max):
                number -= max

            while (number < min):
                number += max

            return number

        if (MutationKa):
            #будет мутация?
            if (random.randint(0, 10000) <= MutationChance):
                #количество мутаций
                NumMut = random.randint(1, 10)
                for i in range(0, NumMut):
                    #МУТАЦИЯ "ГЕНА"
                    self.pram[random.randint(0, len(self.pram)-1)] = random.randint(0, len(self.pram)-1)


    def tic(self, visionSmall):
        #DATA BEGIN
        DATA_SPACE = 0   #0000..0000
        DATA_EAT = 20    #0001..0020
        DATA_BLOCK = 30  #0021..0030
        DATA_CELL = 8899 #8800..8888
        DATA_BOT = 9999  #9900..9999
        #DATA END
        #JUMPS: BLOCKS, BOTS, CELL, EAT, SPACE,
        #  0      +1     +2    +3   +4    +5

        SEEK = visionSmall
        #зрение с кронкой = 1
        #[ [0, 0, 0],   |2D array [Y][X]
        #  [0, 0, 0],
        #  [0, 0, 0] ]

        def LOOK_SEEK(c):
            #0 1 2
            #7   3
            #6 5 4
            x = 0
            y = 0

            if (c == 1):
                x = 1
                y = 0
            elif (c == 2):
                x = 2
                y = 0
            elif (c == 3):
                x = 2
                y = 1
            elif (c == 4):
                x = 2
                y = 2
            elif (c == 5):
                x = 1
                y = 2
            elif (c == 6):
                x = 0
                y = 2
            elif (c == 7):
                x = 0
                y = 1

            return SEEK[y][x]

        def SPACE_CHECK(c):
            #0 1 2
            #7   3
            #6 5 4
            x = 0
            y = 0

            if (c == 0):
                x = -1
                y = -1
            elif (c == 1):
                x = 0
                y = -1
            elif (c == 2):
                x = 1
                y = -1
            elif (c == 3):
                x = 1
                y = 0
            elif (c == 4):
                x = 1
                y = 1
            elif (c == 5):
                x = 0
                y = 1
            elif (c == 6):
                x = -1
                y = 1
            elif (c == 7):
                x = -1
                y = 0

            return x, y

        def Check(number, min, max):
            while (number >= max):
                number -= max

            while (number < min):
                number += max

            return number
        ############################################
        def CheckMEM(number):
            min = 0
            max = len(self.pram)

            while (number >= max):
                number -= max

            while (number < min):
                number += max

            return number
        #############################################
        #INIT
        #move IN
        self.MOVE_X = 0
        self.MOVE_Y = 0

        #REPL
        self.REPL_X = 0
        self.REPL_Y = 0
        self.REPL_STATE = 0 #0 - NOPE; 1 - REPL EN; -1 - DEATH

        #DOAC
        self.DOAC_X = 0
        self.DOAC_Y = 0
        self.DOAC_C = 0 #positive action and negative action and 0 is NOPE
        #############################################
        #0..7 - СДЕЛАТЬ ШАГ
        #8..15 - УДАРИТЬ
        #16..23 - ПОМОЧЬ
        #24..31 - ПОСМОТРЕТЬ
        #32..39 - СДЕЛАТЬ КОПИЮ
        #40 - ВОЗВРАТ
        #41..255 - БЕЗУСЛОВНЫЙ ПЕРЕХОД

        #JUMPS: BLOCKS, BOTS, CELL, EAT, SPACE,
        #  0      +1     +2    +3   +4    +5
        if (self.RED_flag):
            self.stack = self.pc
            self.pc = self.RED + self.RED_pmtr

        if (self.BLU_flag):
            self.stack = self.pc
            self.pc = self.BLU + self.BLU_pmtr

        code = self.pram[self.pc]
        #==============================
        if (code <= 7):
            arr = SPACE_CHECK(code % 8)
            self.MOVE_X = arr[0]
            self.MOVE_Y = arr[1]
        #==============================
        elif (code <= 15):
            arr = SPACE_CHECK(code % 8)
            self.DOAC_X = arr[0]
            self.DOAC_Y = arr[1]
            self.DOAC_C = -1
        #==============================
        elif (code <= 23):
            arr = SPACE_CHECK(code % 8)
            self.DOAC_X = arr[0]
            self.DOAC_Y = arr[1]
            self.DOAC_C = 1
        #==============================
        elif (code <= 31):
            object = LOOK_SEEK(code % 8)
            if (object == DATA_SPACE):
                self.pc = self.pram[CheckMEM(self.pc + 5)]
                ContinueKa = True
            elif (object <= DATA_EAT):
                self.pc = self.pram[CheckMEM(self.pc + 4)]
                ContinueKa = True
            elif (object <= DATA_BLOCK):
                self.pc = self.pram[CheckMEM(self.pc + 1)]
                ContinueKa = True
            elif (object >= (DATA_CELL-99) and object <= DATA_CELL):
                self.pc = self.pram[CheckMEM(self.pc + 3)]
                ContinueKa = True
            elif (object >= (DATA_BOT-99) and object <= DATA_BOT):
                self.pc = self.pram[CheckMEM(self.pc + 2)]
        #==============================
        elif (code <= 39):
            arr = SPACE_CHECK(code % 8)
            self.REPL_X = arr[0]
            self.REPL_Y = arr[1]
            self.REPL_STATE = 1
        #==============================
        elif (code == 40):
            self.pc = self.stack
        elif (code <= 255):
            self.pc = CheckMEM(self.pc + code)

        #############################################
        self.pc = CheckMEM(self.pc + 1)
        self.age += 1
        self.healPoint -= self.CMhangry

        #if (self.healPoint > 300):
        #    self.healPoint = 300

        if (self.healPoint <= 0):
            self.REPL_STATE = -1
        #===FIX VALUES==========================================================
        #===FIX VALUES==========================================================
        if (self.MOVE_X > 0):
            self.MOVE_X = 1
        elif (self.MOVE_X < 0):
            self.MOVE_X = -1

        if (self.MOVE_Y > 0):
            self.MOVE_Y = 1
        elif (self.MOVE_Y < 0):
            self.MOVE_Y = -1

        if (self.REPL_X > 0):
            self.REPL_X = 1
        elif (self.REPL_X < 0):
            self.REPL_X = -1

        if (self.REPL_Y > 0):
            self.REPL_Y = 1
        elif (self.REPL_Y < 0):
            self.REPL_Y = -1

        if (self.DOAC_X > 0):
            self.DOAC_X = 1
        elif (self.DOAC_X < 0):
            self.DOAC_X = -1

        if (self.DOAC_Y > 0):
            self.DOAC_Y = 1
        elif (self.DOAC_Y < 0):
            self.DOAC_Y = -1

        self.RED_flag = False
        self.RED_pmtr = 0
        self.BLU_flag = False
        self.BLU_pmtr = 0

        #===SEND OUTPUT DATA====================================================
        return self.MOVE_X, self.MOVE_Y, self.REPL_X, self.REPL_Y, self.REPL_STATE, self.DOAC_X, self.DOAC_Y, self.DOAC_C
