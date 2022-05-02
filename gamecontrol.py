import math
import random


class GameMaster:
    def __init__(self):
        self.playernumber = int(input("How many Players are on the table? (1-8)"))
        self.handclasses = ["HIGH", "PAIR", "TWOPAIR", "THREEKIND", "STRAIGHT", "FULLCOURT", "ROYALCOURT", "TRIP7"]

    def createtable(self):
        x=1


class PlayerKylo:
    def __init__(self):
        self.ranks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
        self.kings = ["F_King", "M_King", "S_King", "D_King"]
        self.princes = ["F_Prince", "M_Prince", "S_Prince", "D_Prince"]
        self.knights = ["F_Knight", "M_Knight", "S_Knight", "D_Knight"]
        self.sevens = ["7", "7", "7", "7"]
        self.sixes = ["6", "6", "6", "6"]
        self.fives = ["5", "5", "5", "5"]
        self.fours = ["4", "4", "4", "4"]
        self.threes = ["3", "3", "3", "3"]
        self.twos = ["2", "2", "2", "2"]
        self.ones = ["1", "1", "1", "1"]
        self.agents = ["Assassin", "Assassin", "Thief"]


    def shuffle(self):
        shuffled_deck = []

        totaldeck = self.kings+self.princes+self.knights+self.sevens+self.sixes+self.fives+self.fours+self.threes+\
                    self.twos+self.ones+self.agents

        cardstoshuffle = len(totaldeck)

        lookingat = 0
        rankused = random.randrange(0, 11)
        cardsshuffled = 0
        numberofattempts=0

        while cardsshuffled < cardstoshuffle:
            match rankused:
                case 0:
                    lookingat = random.randrange(0, len(self.agents))
                    if self.agents[lookingat] != 0:
                        shuffled_deck.append(self.agents[lookingat])
                        self.agents[lookingat] = 0
                        cardsshuffled+=1
                case 1:
                    lookingat = random.randrange(0, len(self.ones))
                    if self.ones[lookingat] != 0:
                        shuffled_deck.append(self.ones[lookingat])
                        self.ones[lookingat] = 0
                        cardsshuffled += 1
                case 2:
                    lookingat = random.randrange(0, len(self.twos))
                    if self.twos[lookingat] != 0:
                        shuffled_deck.append(self.twos[lookingat])
                        self.twos[lookingat] = 0
                        cardsshuffled += 1
                case 3:
                    lookingat = random.randrange(0, len(self.threes))
                    if self.threes[lookingat] != 0:
                        shuffled_deck.append(self.threes[lookingat])
                        self.threes[lookingat] = 0
                        cardsshuffled += 1
                case 4:
                    lookingat = random.randrange(0, len(self.fours))
                    if self.fours[lookingat] != 0:
                        shuffled_deck.append(self.fours[lookingat])
                        self.fours[lookingat] = 0
                        cardsshuffled += 1
                case 5:
                    lookingat = random.randrange(0, len(self.fives))
                    if self.fives[lookingat] != 0:
                        shuffled_deck.append(self.fives[lookingat])
                        self.fives[lookingat] = 0
                        cardsshuffled += 1
                case 6:
                    lookingat = random.randrange(0, len(self.sixes))
                    if self.sixes[lookingat] != 0:
                        shuffled_deck.append(self.sixes[lookingat])
                        self.sixes[lookingat] = 0
                        cardsshuffled += 1
                case 7:
                    lookingat = random.randrange(0, len(self.sevens))
                    if self.sevens[lookingat] != 0:
                        shuffled_deck.append(self.sevens[lookingat])
                        self.sevens[lookingat] = 0
                        cardsshuffled += 1
                case 8:
                    lookingat = random.randrange(0, len(self.knights))
                    if self.knights[lookingat] != 0:
                        shuffled_deck.append(self.knights[lookingat])
                        self.knights[lookingat] = 0
                        cardsshuffled += 1
                case 9:
                    lookingat = random.randrange(0, len(self.princes))
                    if self.princes[lookingat] != 0:
                        shuffled_deck.append(self.princes[lookingat])
                        self.princes[lookingat] = 0
                        cardsshuffled += 1
                case 10:
                    lookingat = random.randrange(0, len(self.kings))
                    if self.kings[lookingat] != 0:
                        shuffled_deck.append(self.kings[lookingat])
                        self.kings[lookingat] = 0
                        cardsshuffled += 1

            rankused = random.randrange(0, 11)
            numberofattempts+=1

        print("shuffler ran: ", numberofattempts, " times!")
        return shuffled_deck


class Table:
    def __init__(self, EMPEROR, taxcart, CommunityCards, Player1, Player2, Player3, Player4, Player5, Player6 ,Player7 ,
                 Player8 ):
        self.EMPEROR = EMPEROR
        self.taxcart = taxcart
        self.CommunityCards = CommunityCards
        self.Player1 = Player1
        self.Player2 = Player2
        self.Player3 = Player3
        self.Player4 = Player4
        self.Player5 = Player5
        self.Player6 = Player6
        self.Player7 = Player7
        self.Player8 = Player8


class Player:
    def __init__(self, name, startbank=100):
        self.name = name
        self.bank = int(startbank)
        self.hand = list([])
        self.carddown = str("")


class HandClass:
    def __init__(self, classnames, frequency):
        self.name =classnames
        self.frequency = frequency


def deal(shuffleddeck, handbeingdealt, cardsdealt):
    hand = handbeingdealt
    hand.append(shuffleddeck[cardsdealt])
    return hand
