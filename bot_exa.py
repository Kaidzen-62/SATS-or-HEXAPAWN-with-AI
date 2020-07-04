import random

class R8BE():
    def __init__(self, x, y, id, PC, PRAM, RAMM, CMhangry, MutationKa, MutationChance):
        self.id = id
        self.x = x
        self.y = y
        #programm memory
        self.pram = PRAM
        #mutation % memory
        self.ramm = RAMM

        #val memory
        self.ram = []
        for i in range(0, 19999):
            self.ram.append(0)

        self.MutationKa = MutationKa

        #=======================================================================
        self.age = 0
        self.happy = 100
        self.healPoint = 100
        self.hangry = 200
        self.CMhangry = CMhangry
        self.inventory = 0

        self.code = [0,0,0,0]
        self.pc = PC

        #САМОЕ_ВКУСНЕНЬКОЕ======================================================
        #РЕГИСТРЫ ВХОДА/ВЫХОДЯ И ДЕЙСТВИЯ
        #move IN
        self.MOVE_X = 0
        self.MOVE_Y = 0

        #REPL
        self.REPL_X = 0
        self.REPL_Y = 0
        self.REPL_PC = 0
        self.REPL_STATE = 0 #0 - NOPE; 1 - REPL EN; -1 - DEATH

        #DOAC
        self.DOAC_X = 0
        self.DOAC_Y = 0
        self.DOAC_C = 0 #positive action and negative action and 0 is NOPE

        #RADIO SPEECH
        self.RDOS_VAL = 0
        self.RDIS_HZ = 2000

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
                NumMut = random.randint(0, 16)
                for i in range(0, NumMut):
                    #тип мутации
                    type = random.randint(0, 4)
                    #какая строчка кода подвергнется мутации?
                    line = 0
                    line_found = False
                    PPP = 0
                    while (not(line_found)):
                        PPP += 1
                        if (PPP >= 19997):
                            break

                        line = random.randint(0, 19998)
                        if (random.randint(0, 10000) <= ((self.ramm[line][0] + self.ramm[line][1] + self.ramm[line][2] + self.ramm[line][3]) // 4) and type == 0):
                            line_found = True
                        elif (type == 1 and random.randint(0, 10000) <= self.ramm[line][1]):
                            line_found = True
                        elif (type == 2 and random.randint(0, 10000) <= self.ramm[line][2]):
                            line_found = True
                        elif (type == 3 and random.randint(0, 10000) <= self.ramm[line][3]):
                            line_found = True
                        elif (type == 4 and random.randint(0, 10000) <= self.ramm[line][0]):
                            line_found = True
                        else:
                            if (self.ramm[line][0] > 0):
                                self.ramm[line][0] -= 1
                            if (self.ramm[line][1] > 0):
                                self.ramm[line][1] -= 1
                            if (self.ramm[line][2] > 0):
                                self.ramm[line][2] -= 1
                            if (self.ramm[line][3] > 0):
                                self.ramm[line][3] -= 1

                    #мутация всей строки
                    if (type == 0):
                        self.pram[line][0] = random.randint(0, 88)
                        self.pram[line][1] = random.randint(-9999, 9999)
                        self.pram[line][2] = random.randint(-9999, 9999)
                        self.pram[line][3] = random.randint(-9999, 9999)

                        if (self.ramm[line][0] < 10000):
                            self.ramm[line][0] += 1
                        if (self.ramm[line][1] < 10000):
                            self.ramm[line][1] += 1
                        if (self.ramm[line][2] < 10000):
                            self.ramm[line][2] += 1
                        if (self.ramm[line][3] < 10000):
                            self.ramm[line][3] += 1
                    #мутация первой переменной
                    elif (type == 1):
                        self.pram[line][1] = random.randint(-9999, 9999)

                        if (self.ramm[line][1] < 10000):
                            self.ramm[line][1] += 1
                    #мутация второй переменной
                    elif (type == 2):
                        self.pram[line][2] = random.randint(-9999, 9999)

                        if (self.ramm[line][2] < 10000):
                            self.ramm[line][2] += 1
                    #мутация третьей переменной
                    elif (type == 3):
                        self.pram[line][3] = random.randint(-9999, 9999)

                        if (self.ramm[line][3] < 10000):
                            self.ramm[line][3] += 1
                    #мутация команды
                    elif (type == 4):
                        self.pram[line][0] = random.randint(0, 88)

                        if (self.ramm[line][0] < 10000):
                            self.ramm[line][0] += 1


    def tic(self, visionSmall, visionFull, ETHER):
        #зрение с кронкой = 3
        #00 01 02 03 04 |12 - всегда = 9999
        #05 06 07 08 09
        #10 11 12 13 14
        #15 16 17 18 19
        #20 21 22 23 24
        SEEG = visionFull
        #зрение с кронкой = 1
        #[ [0, 0, 0],   |2D array [Y][X]
        #  [0, 0, 0],
        #  [0, 0, 0] ]
        SEEK = visionSmall

        def LOOK_SEEK(x, y):
            if (x > 0):
                x = 2
            elif (x < 0):
                x = 0
            else:
                x = 1

            if (y > 0):
                y = 2
            elif (y < 0):
                y = 0
            else:
                y = 1

            return SEEK[y][x]

        def Check(number, min, max):
            while (number >= max):
                number -= max

            while (number < min):
                number += max

            return number
        ############################################
        def CheckMEM(number):
            #от -9999 0 9999
            min = -9999
            max = 9999

            while (number > max):
                number -= 19999

            while (number < min):
                number += 19999

            return number
        #############################################
        def PC_CHECK(number):
            return 9999 + number
        #############################################
        def PC_SCHECK(number):
            return PC_CHECK(CheckMEM(number))
        #############################################
        #INIT
        #move IN
        self.MOVE_X = 0
        self.MOVE_Y = 0

        #REPL
        self.REPL_X = 0
        self.REPL_Y = 0
        self.REPL_PC = 0
        self.REPL_STATE = 0 #0 - NOPE; 1 - REPL EN; -1 - DEATH

        #DOAC
        self.DOAC_X = 0
        self.DOAC_Y = 0
        self.DOAC_C = 0 #positive action and negative action and 0 is NOPE
        #=======================================================================
        #PRAM VAL:   -9999..0..9999
        #PRAM ADRES: 0..19998  (-9999 = 0; 9999 = 19998)
        #=======================================================================
        #begin#######################################



        #cpu-emu#####################################

        #==============================================
        #read CMD
        self.code[0] = self.pram[PC_CHECK(self.pc)][0]
        #read VAL1
        self.code[1] = self.pram[PC_CHECK(self.pc)][1]
        #read VAL2
        self.code[2] = self.pram[PC_CHECK(self.pc)][2]
        #read VAL3
        self.code[3] = self.pram[PC_CHECK(self.pc)][3]
        #==============================================

        #NOPE===================================================================
        #self.code[0] == 0
        #MOVE===================================================================
        #MOVE NN
        if (self.code[0] == 1):
            self.MOVE_X = self.code[1]
            self.MOVE_Y = self.code[2]

            self.happy += self.CMhangry
        #MOVE AN
        elif (self.code[0] == 2):
            self.MOVE_X = self.ram[PC_CHECK(self.code[1])]
            self.MOVE_Y = self.code[2]

            self.happy += self.CMhangry
        #MOVE NA
        elif (self.code[0] == 3):
            self.MOVE_X = self.code[1]
            self.MOVE_Y = self.ram[PC_CHECK(self.code[2])]

            self.happy += self.CMhangry
        #MOVE AA
        elif (self.code[0] == 4):
            self.MOVE_Y = self.ram[PC_CHECK(self.code[1])]
            self.MOVE_Y = self.ram[PC_CHECK(self.code[2])]

            self.happy += self.CMhangry
        #SEEK===================================================================
        #SEEK NN
        elif (self.code[0] == 5):
            self.ram[PC_CHECK(self.code[3])] = LOOK_SEEK(self.code[1], self.code[2])
        #SEEK NA
        elif (self.code[0] == 6):
            self.ram[PC_CHECK(self.code[3])] = LOOK_SEEK(self.code[1], self.ram[PC_CHECK(self.code[2])])
        #SEEK AN
        elif (self.code[0] == 7):
            self.ram[PC_CHECK(self.code[3])] = LOOK_SEEK(self.ram[PC_CHECK(self.code[1])], self.code[2])
        #SEEK AA
        elif (self.code[0] == 8):
            self.ram[PC_CHECK(self.code[3])] = LOOK_SEEK(self.ram[PC_CHECK(self.code[1])], self.ram[PC_CHECK(self.code[2])])
        #SEEG===================================================================
        #SEEG N
        elif (self.code[0] == 9):
            self.ram[PC_CHECK(self.code[2])] = SEEG[Check(self.code[1], 0, 25)]
        #SEEG A
        elif (self.code[0] == 10):
            self.ram[PC_CHECK(self.code[2])] = SEEG[Check(self.ram[PC_CHECK(self.code[1])], 0, 25)]
        #DOAC===================================================================
        #DOAC NNN
        elif (self.code[0] == 11):
            self.DOAC_X = self.code[1]
            self.DOAC_Y = self.code[2]
            self.DOAC_C = self.code[3]

            self.happy += self.CMhangry * 3
        #DOAC NNA
        elif (self.code[0] == 12):
            self.DOAC_X = self.code[1]
            self.DOAC_Y = self.code[2]
            self.DOAC_C = self.ram[PC_CHECK(self.code[3])]

            self.happy += self.CMhangry * 3
        #DOAC NAN
        elif (self.code[0] == 13):
            self.DOAC_X = self.code[1]
            self.DOAC_Y = self.ram[PC_CHECK(self.code[2])]
            self.DOAC_C = self.code[3]

            self.happy += self.CMhangry * 3
        #DOAC NAA
        elif (self.code[0] == 14):
            self.DOAC_X = self.code[1]
            self.DOAC_Y = self.ram[PC_CHECK(self.code[2])]
            self.DOAC_C = self.ram[PC_CHECK(self.code[3])]

            self.happy += self.CMhangry * 3
        #DOAC ANN
        elif (self.code[0] == 15):
            self.DOAC_X = self.ram[PC_CHECK(self.code[1])]
            self.DOAC_Y = self.code[2]
            self.DOAC_C = self.code[3]

            self.happy += self.CMhangry * 3
        #DOAC ANA
        elif (self.code[0] == 16):
            self.DOAC_X = self.ram[PC_CHECK(self.code[1])]
            self.DOAC_Y = self.code[2]
            self.DOAC_C = self.ram[PC_CHECK(self.code[3])]

            self.happy += self.CMhangry * 3
        #DOAC AAN
        elif (self.code[0] == 17):
            self.DOAC_X = self.ram[PC_CHECK(self.code[1])]
            self.DOAC_Y = self.ram[PC_CHECK(self.code[2])]
            self.DOAC_C = self.code[3]

            self.happy += self.CMhangry * 3
        #DOAC AAA
        elif (self.code[0] == 18):
            self.DOAC_X = self.ram[PC_CHECK(self.code[1])]
            self.DOAC_Y = self.ram[PC_CHECK(self.code[2])]
            self.DOAC_C = self.ram[PC_CHECK(self.code[3])]

            self.happy += self.CMhangry * 3
        #REPL===================================================================
        #REPL NNN
        elif (self.code[0] == 19):
            self.REPL_X = self.code[1]
            self.REPL_Y = self.code[2]
            self.REPL_PC = self.code[3]
            self.REPL_STATE = 1

            #self.hangry -= 100#self.CMhangry * 3
            self.happy += self.CMhangry * 10
        #REPL NNA
        elif (self.code[0] == 20):
            self.REPL_X = self.code[1]
            self.REPL_Y = self.code[2]
            self.REPL_PC = self.ram[PC_CHECK(self.code[3])]
            self.REPL_STATE = 1

            #self.hangry -= 100#self.CMhangry * 3
            self.happy += self.CMhangry * 10
        #REPL NAN
        elif (self.code[0] == 21):
            self.REPL_X = self.code[1]
            self.REPL_Y = self.ram[PC_CHECK(self.code[2])]
            self.REPL_PC = self.code[3]
            self.REPL_STATE = 1

            #self.hangry -= 100#self.CMhangry * 3
            self.happy += self.CMhangry * 10
        #REPL NAA
        elif (self.code[0] == 22):
            self.REPL_X = self.code[1]
            self.REPL_Y = self.ram[PC_CHECK(self.code[2])]
            self.REPL_PC = self.ram[PC_CHECK(self.code[3])]
            self.REPL_STATE = 1

            #self.hangry -= 100#self.CMhangry * 3
            self.happy += self.CMhangry * 10
        #REPL ANN
        elif (self.code[0] == 23):
            self.REPL_X = self.ram[PC_CHECK(self.code[1])]
            self.REPL_Y = self.code[2]
            self.REPL_PC = self.code[3]
            self.REPL_STATE = 1

            #self.hangry -= 100#self.CMhangry * 3
            self.happy += self.CMhangry * 10
        #REPL ANA
        elif (self.code[0] == 24):
            self.REPL_X = self.ram[PC_CHECK(self.code[1])]
            self.REPL_Y = self.code[2]
            self.REPL_PC = self.ram[PC_CHECK(self.code[3])]
            self.REPL_STATE = 1

            #self.hangry -= 100#self.CMhangry * 3
            self.happy += self.CMhangry * 10
        #REPL AAN
        elif (self.code[0] == 25):
            self.REPL_X = self.ram[PC_CHECK(self.code[1])]
            self.REPL_Y = self.ram[PC_CHECK(self.code[2])]
            self.REPL_PC = self.code[3]
            self.REPL_STATE = 1

            #self.hangry -= 100# self.CMhangry * 3
            self.happy += self.CMhangry * 10
        #REPL AAA
        elif (self.code[0] == 26):
            self.REPL_X = self.ram[PC_CHECK(self.code[1])]
            self.REPL_Y = self.ram[PC_CHECK(self.code[2])]
            self.REPL_PC = self.ram[PC_CHECK(self.code[3])]
            self.REPL_STATE = 1

            #self.hangry -= 33#self.CMhangry * 3
            self.happy += self.CMhangry * 10
        #RDIS===================================================================
        #RDIS AN
        elif (self.code[0] == 27):
            self.ram[PC_CHECK(self.code[1])] = ETHER[PC_CHECK(self.code[2])]
        #RDIS AA
        elif (self.code[0] == 28):
            self.ram[PC_CHECK(self.code[1])] = ETHER[PC_CHECK(self.ram[PC_CHECK(self.code[2])])]
        #RDOS===================================================================
        #RDOS NN
        elif (self.code[0] == 29):
            self.RDOS_VAL = self.code[1]
            self.RDIS_HZ = PC_CHECK(self.code[2])
        #RDOS NA
        elif (self.code[0] == 30):
            self.RDOS_VAL = self.code[1]
            self.RDIS_HZ = PC_CHECK(self.ram[PC_CHECK(self.code[2])])
        #RDOS AN
        elif (self.code[0] == 31):
            self.RDOS_VAL = self.ram[PC_CHECK(self.code[1])]
            self.RDIS_HZ = PC_CHECK(self.code[2])
        #RDOS AA
        elif (self.code[0] == 32):
            self.RDOS_VAL = self.ram[PC_CHECK(self.code[1])]
            self.RDIS_HZ = PC_CHECK(self.ram[PC_CHECK(self.code[2])])
        #STVR===================================================================
        #STRV NA
        elif (self.code[0] == 33):
            self.ram[PC_CHECK(self.code[2])] = self.code[1]
        #STRV AA
        elif (self.code[0] == 34):
            self.ram[PC_CHECK(self.code[2])] = self.ram[PC_CHECK(self.code[1])]
        #LDRI===================================================================
        #LDRI NA
        elif (self.code[0] == 35):
            self.pram[PC_CHECK(self.code[2])][0] = Check(self.code[1], 0, 89)
        #LDRI AA
        elif (self.code[0] == 36):
            self.pram[PC_CHECK(self.code[2])][0] = Check(self.ram[PC_CHECK(self.code[1])], 0, 89)
        #LDRX===================================================================
        #LDRX NA
        elif (self.code[0] == 37):
            self.pram[PC_CHECK(self.code[2])][1] = self.code[1]
        #LDRX AA
        elif (self.code[0] == 38):
            self.pram[PC_CHECK(self.code[2])][1] = self.ram[PC_CHECK(self.code[1])]
        #LDRY===================================================================
        #LDRY NA
        elif (self.code[0] == 39):
            self.pram[PC_CHECK(self.code[2])][2] = self.code[1]
        #LDRY AA
        elif (self.code[0] == 40):
            self.pram[PC_CHECK(self.code[2])][2] = self.ram[PC_CHECK(self.code[1])]
        #LDRC===================================================================
        #LDRC NA
        elif (self.code[0] == 41):
            self.pram[PC_CHECK(self.code[2])][3] = self.code[1]
        #LDRC AA
        elif (self.code[0] == 42):
            self.pram[PC_CHECK(self.code[2])][3] = self.ram[PC_CHECK(self.code[1])]
        #ADDI===================================================================
        #ADDI NNA
        elif (self.code[0] == 43):
            self.ram[PC_CHECK(self.code[3])] = self.code[1] + self.code[2]
        #ADDI NAA
        elif (self.code[0] == 44):
            self.ram[PC_CHECK(self.code[3])] = self.code[1] + self.ram[PC_CHECK(self.code[2])]
        #ADDI ANA
        elif (self.code[0] == 45):
            self.ram[PC_CHECK(self.code[3])] = self.ram[PC_CHECK(self.code[1])] + self.code[2]
        #ADDI AAA
        elif (self.code[0] == 46):
            self.ram[PC_CHECK(self.code[3])] = self.ram[PC_CHECK(self.code[1])] + self.ram[PC_CHECK(self.code[2])]
        #SUBI===================================================================
        #SUBI NNA
        elif (self.code[0] == 47):
            self.ram[PC_CHECK(self.code[3])] = self.code[1] - self.code[2]
        #SUBI NAA
        elif (self.code[0] == 48):
            self.ram[PC_CHECK(self.code[3])] = self.code[1] - self.ram[PC_CHECK(self.code[2])]
        #SUBI ANA
        elif (self.code[0] == 49):
            self.ram[PC_CHECK(self.code[3])] = self.ram[PC_CHECK(self.code[1])] - self.code[2]
        #SUBI AAA
        elif (self.code[0] == 50):
            self.ram[PC_CHECK(self.code[3])] = self.ram[PC_CHECK(self.code[1])] - self.ram[PC_CHECK(self.code[2])]
        #MULI===================================================================
        #MULI NNA
        elif (self.code[0] == 51):
            self.ram[PC_CHECK(self.code[3])] = self.code[1] * self.code[2]
        #MULI NAA
        elif (self.code[0] == 52):
            self.ram[PC_CHECK(self.code[3])] = self.code[1] * self.ram[PC_CHECK(self.code[2])]
        #MULI ANA
        elif (self.code[0] == 53):
            self.ram[PC_CHECK(self.code[3])] = self.ram[PC_CHECK(self.code[1])] * self.code[2]
        #MULI AAA
        elif (self.code[0] == 54):
            self.ram[PC_CHECK(self.code[3])] = self.ram[PC_CHECK(self.code[1])] * self.ram[PC_CHECK(self.code[2])]
        #DIVI===================================================================
        #DIVI NNA
        elif (self.code[0] == 55):
            if (self.code[2] != 0):
                self.ram[PC_CHECK(self.code[3])] = self.code[1] // self.code[2]
            else:
                self.ram[PC_CHECK(self.code[3])] = 9999
        #DIVI NAA
        elif (self.code[0] == 56):
            if (self.ram[PC_CHECK(self.code[2])] != 0):
                self.ram[PC_CHECK(self.code[3])] = self.code[1] // self.ram[PC_CHECK(self.code[2])]
            else:
                self.ram[PC_CHECK(self.code[3])] = 9999
        #DIVI ANA
        elif (self.code[0] == 57):
            if (self.code[2] != 0):
                self.ram[PC_CHECK(self.code[3])] = self.ram[PC_CHECK(self.code[1])] // self.code[2]
            else:
                self.ram[PC_CHECK(self.code[3])] = 9999
        #DIVI AAA
        elif (self.code[0] == 58):
            if (self.ram[PC_CHECK(self.code[2])] != 0):
                self.ram[PC_CHECK(self.code[3])] = self.ram[PC_CHECK(self.code[1])] // self.ram[PC_CHECK(self.code[2])]
            else:
                self.ram[PC_CHECK(self.code[3])] = 9999
        #MODI===================================================================
        #MODI NNA
        elif (self.code[0] == 55):
            if (self.code[2] != 0):
                self.ram[PC_CHECK(self.code[3])] = self.code[1] % self.code[2]
            else:
                self.ram[PC_CHECK(self.code[3])] = 9999
        #MODI NAA
        elif (self.code[0] == 56):
            if (self.ram[PC_CHECK(self.code[2])] != 0):
                self.ram[PC_CHECK(self.code[3])] = self.code[1] % self.ram[PC_CHECK(self.code[2])]
            else:
                self.ram[PC_CHECK(self.code[3])] = 9999
        #MODI ANA
        elif (self.code[0] == 57):
            if (self.code[2] != 0):
                self.ram[PC_CHECK(self.code[3])] = self.ram[PC_CHECK(self.code[1])] % self.code[2]
            else:
                self.ram[PC_CHECK(self.code[3])] = 9999
        #MODI AAA
        elif (self.code[0] == 58):
            if (self.ram[PC_CHECK(self.code[2])] != 0):
                self.ram[PC_CHECK(self.code[3])] = self.ram[PC_CHECK(self.code[1])] % self.ram[PC_CHECK(self.code[2])]
            else:
                self.ram[PC_CHECK(self.code[3])] = 9999
        #JUMP===================================================================
        #JUMP N
        elif (self.code[0] == 63):
            self.pc = self.code[1] -1
        #JUMP A
        elif (self.code[0] == 64):
            self.pc = self.ram[PC_CHECK(self.code[1])] -1
        #JALZ===================================================================
        #JALZ AN
        elif (self.code[0] == 65):
            if (self.ram[PC_CHECK(self.code[1])] < 0):
                self.pc = self.code[2] -1
        #JALZ AA
        elif (self.code[0] == 66):
            if (self.ram[PC_CHECK(self.code[1])] < 0):
                self.pc = self.ram[PC_CHECK(self.code[2])] -1
        #JAGZ===================================================================
        #JAGZ AN
        elif (self.code[0] == 67):
            if (self.ram[PC_CHECK(self.code[1])] > 0):
                self.pc = self.code[2] -1
        #JAGZ AA
        elif (self.code[0] == 68):
            if (self.ram[PC_CHECK(self.code[1])] > 0):
                self.pc = self.ram[PC_CHECK(self.code[2])] -1
        #JAEZ===================================================================
        #JAEZ AN
        elif (self.code[0] == 69):
            if (self.ram[PC_CHECK(self.code[1])] == 0):
                self.pc = self.code[2] -1
        #JAEZ AA
        elif (self.code[0] == 70):
            if (self.ram[PC_CHECK(self.code[1])] == 0):
                self.pc = self.ram[PC_CHECK(self.code[2])] -1
        #JALA===================================================================
        #JALA NAN
        elif (self.code[0] == 71):
            if (self.code[1] < self.ram[PC_CHECK(self.code[2])]):
                self.pc = self.code[3] -1
        #JALA ANN
        elif (self.code[0] == 72):
            if (self.ram[PC_CHECK(self.code[1])] < self.code[2]):
                self.pc = self.code[3] -1
        #JALA AAN
        elif (self.code[0] == 73):
            if (self.ram[PC_CHECK(self.code[1])] < self.ram[PC_CHECK(self.code[2])]):
                self.pc = self.code[3] -1

        #JALA NAA
        elif (self.code[0] == 74):
            if (self.code[1] < self.ram[PC_CHECK(self.code[2])]):
                self.pc = self.ram[PC_CHECK(self.code[3])] -1
        #JALA ANA
        elif (self.code[0] == 75):
            if (self.ram[PC_CHECK(self.code[1])] < self.code[2]):
                self.pc = self.ram[PC_CHECK(self.code[3])] -1
        #JALA AAA
        elif (self.code[0] == 76):
            if (self.ram[PC_CHECK(self.code[1])] < self.ram[PC_CHECK(self.code[2])]):
                self.pc = self.ram[PC_CHECK(self.code[3])] -1
        #JAGA===================================================================
        #JAGA NAN
        elif (self.code[0] == 77):
            if (self.code[1] > self.ram[PC_CHECK(self.code[2])]):
                self.pc = self.code[3] -1
        #JAGA ANN
        elif (self.code[0] == 78):
            if (self.ram[PC_CHECK(self.code[1])] > self.code[2]):
                self.pc = self.code[3] -1
        #JAGA AAN
        elif (self.code[0] == 79):
            if (self.ram[PC_CHECK(self.code[1])] > self.ram[PC_CHECK(self.code[2])]):
                self.pc = self.code[3] -1

        #JAGA NAA
        elif (self.code[0] == 80):
            if (self.code[1] > self.ram[PC_CHECK(self.code[2])]):
                self.pc = self.ram[PC_CHECK(self.code[3])] -1
        #JAGA ANA
        elif (self.code[0] == 81):
            if (self.ram[PC_CHECK(self.code[1])] > self.code[2]):
                self.pc = self.ram[PC_CHECK(self.code[3])] -1
        #JAGA AAA
        elif (self.code[0] == 82):
            if (self.ram[PC_CHECK(self.code[1])] > self.ram[PC_CHECK(self.code[2])]):
                self.pc = self.ram[PC_CHECK(self.code[3])] -1
        #JAEA===================================================================
        #JAEA NAN
        elif (self.code[0] == 83):
            if (self.code[1] == self.ram[PC_CHECK(self.code[2])]):
                self.pc = self.code[3] -1
        #JAEA ANN
        elif (self.code[0] == 84):
            if (self.ram[PC_CHECK(self.code[1])] == self.code[2]):
                self.pc = self.code[3] -1
        #JAEA AAN
        elif (self.code[0] == 85):
            if (self.ram[PC_CHECK(self.code[1])] == self.ram[PC_CHECK(self.code[2])]):
                self.pc = self.code[3] -1

        #JAEA NAA
        elif (self.code[0] == 86):
            if (self.code[1] == self.ram[PC_CHECK(self.code[2])]):
                self.pc = self.ram[PC_CHECK(self.code[3])] -1
        #JAEA ANA
        elif (self.code[0] == 87):
            if (self.ram[PC_CHECK(self.code[1])] == self.code[2]):
                self.pc = self.ram[PC_CHECK(self.code[3])] -1
        #JAEA AAA
        elif (self.code[0] == 88):
            if (self.ram[PC_CHECK(self.code[1])] == self.ram[PC_CHECK(self.code[2])]):
                self.pc = self.ram[PC_CHECK(self.code[3])] -1
        #SWIZ===================================================================
        #SWIZ NAA
        elif (self.code[0] == 89):
            key = ''
            var = ''
            out = ''
            kof = 1

            code1 = self.code[1]
            code2 = self.ram[PC_CHECK(self.code[2])]

            if (code1 * code2 < 0):
                kof *= -1

            if (code1 < 0):
                code1 *= -1
            if (code2 < 0):
                code2 *= -1

            var = str(code2)
            var = '0' + var[3] + var[2] + var[1] + var[0]

            key = str(code1)
            key = [ Check(int(key[0]), 0, 5), Check(int(key[1]), 0, 5), Check(int(key[2]), 0, 5), Check(int(key[3]), 0, 5) ]

            out = int(var[key[0]] + var[key[1]] + var[key[2]] + var[key[3]]) * kof

        #SWIZ ANA
        elif (self.code[0] == 90):
            key = ''
            var = ''
            out = ''
            kof = 1

            code1 = self.ram[PC_CHECK(self.code[1])]
            code2 = self.code[2]

            if (code1 * code2 < 0):
                kof *= -1

            if (code1 < 0):
                code1 *= -1
            if (code2 < 0):
                code2 *= -1

            var = str(code2)
            var = '0' + var[3] + var[2] + var[1] + var[0]

            key = str(code1)
            key = [ Check(int(key[0]), 0, 5), Check(int(key[1]), 0, 5), Check(int(key[2]), 0, 5), Check(int(key[3]), 0, 5) ]

            out = int(var[key[0]] + var[key[1]] + var[key[2]] + var[key[3]]) * kof
        #SWIZ AAA
        elif (self.code[0] == 91):
            key = ''
            var = ''
            out = ''
            kof = 1

            code1 = self.ram[PC_CHECK(self.code[1])]
            code2 = self.ram[PC_CHECK(self.code[2])]

            if (code1 * code2 < 0):
                kof *= -1

            if (code1 < 0):
                code1 *= -1
            if (code2 < 0):
                code2 *= -1

            var = str(code2)
            var = '0' + var[3] + var[2] + var[1] + var[0]

            key = str(code1)
            key = [ Check(int(key[0]), 0, 5), Check(int(key[1]), 0, 5), Check(int(key[2]), 0, 5), Check(int(key[3]), 0, 5) ]

            out = int(var[key[0]] + var[key[1]] + var[key[2]] + var[key[3]]) * kof

        #END====================================================================
        self.pc = CheckMEM(self.pc + 1)
        self.age += 1

        self.happy -= self.CMhangry

        if (self.healPoint > 100):
            self.healPoint = 100

        if (self.hangry > 200):
            self.hangry = 200

        if (self.hangry > 0):
            self.hangry -= self.CMhangry
        else:
            self.healPoint += self.hangry
            self.healPoint -= self.CMhangry

        if (self.hangry > 0 and self.healPoint < 100):
            self.healPoint += self.CMhangry
            self.hangry -= self.CMhangry

        if (self.healPoint <= 0):
            self.REPL_STATE = -1

        if (self.happy <= 0):
            self.hangry -= self.CMhangry * 2
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

        if (self.DOAC_C == 666):
            self.DOAC_C = 666
        elif (self.DOAC_C == -666):
            self.DOAC_C = -666
        elif (self.DOAC_C > 0):
            self.DOAC_C = 1
        elif (self.DOAC_C < 0):
            self.DOAC_C = -1

        self.REPL_PC = CheckMEM(self.REPL_PC)


        #===SEND OUTPUT DATA====================================================
        return self.MOVE_X, self.MOVE_Y, self.REPL_X, self.REPL_Y, self.REPL_PC, self.REPL_STATE, self.DOAC_X, self.DOAC_Y, self.DOAC_C, self.RDIS_HZ, self.RDOS_VAL
