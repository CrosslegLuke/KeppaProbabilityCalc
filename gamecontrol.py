import math
import random


class GameMaster:
    def __init__(self):
        self.playernumber = int(input("How many Players are on the table? (1-8)"))
        self.handclasses = ["HIGH", "PAIR", "TWOPAIR", "THREEKIND", "STRAIGHT", "FULLCOURT", "ROYALCOURT", "TRIP7"]

    def create_table(self):
        x=1


class PlayerKylo:
    def __init__(self):
        self.ranks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
        #self.kings = ["F_King", "M_King", "S_King", "D_King"]
        #self.princes = ["F_Prince", "M_Prince", "S_Prince", "D_Prince"]
        #self.knights = ["F_Knight", "M_Knight", "S_Knight", "D_Knight"]
        self.kings =   ["King", "King", "King", "King"]
        self.princes = ["Prince", "Prince", "Prince", "Prince"]
        self.knights = ["Knight", "Knight", "Knight", "Knight"]

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
    def __init__(self, CommunityCards, Player1, Player2, Player3, Player4, Player5, Player6 ,Player7 ,
                 Player8, EMPEROR=0, taxcart=0 ):
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

        self.playerindex = [self.Player1, self.Player2, self.Player3, self.Player4, self.Player5, self.Player6, self.Player7,
                       self.Player8]

    def build_true_hands(self):
        playerid = 0
        playerindex = self.playerindex
        community = self.CommunityCards

        while playerid < len(playerindex):
            playerchanging = playerindex[playerid]
            playerchanging.hand = playerchanging.hand + community
            playerindex[playerid] = playerchanging
            playerid +=1

    def rate_hands(self):
        playerid = 0
        playerindex = self.playerindex

        while playerid < len(playerindex):
            playerchanging = playerindex[playerid]
            clasd = 0
            i=0

            if playerchanging.hand[i] == "King":
                if playerchanging.hand[i+1] == playerchanging.hand[i] and playerchanging.hand[i+2] == playerchanging.hand[i]:
                    clasd = 1
                    break
                elif playerchanging.hand == 3:
                    clasd = 2




class Player:
    def __init__(self, name, startbank=100):
        self.name = name
        self.bank = int(startbank)
        self.hand = list([])
        self.carddown = str("")
        self.Handclass = 0

    def sort_hand(self):
        newhandpos = 0
        newhand = list(self.hand)
        numcard = 7
        i=0

        while newhandpos < len(newhand):
            while i < len(self.hand):
                if newhandpos >= 4:
                    break
                elif self.hand[i] == "F_King" or self.hand[i] == "M_King" or self.hand[i] == "S_King" or self.hand[i] == "D_King":
                    newhand[newhandpos] = self.hand[i]
                    self.hand[i] = ""
                    i = 0
                    newhandpos += 1
                else:
                    i += 1
            i=0
            while i < len(self.hand):
                if newhandpos >= len(newhand):
                    break
                elif self.hand[i] == "F_Prince" or self.hand[i] == "M_Prince" or self.hand[i] == "S_Prince" or self.hand[i] == "D_Prince":
                    newhand[newhandpos] = self.hand[i]
                    self.hand[i] = ""
                    i = 0
                    newhandpos += 1
                else:
                    i += 1
            i = 0
            while i < len(self.hand):
                if newhandpos >= len(newhand):
                    break
                elif self.hand[i] == "F_Knight" or self.hand[i] == "M_Knight" or self.hand[i] == "S_Knight" or self.hand[i] == "D_Knight":
                    newhand[newhandpos] = self.hand[i]
                    self.hand[i] = ""
                    i = 0
                    newhandpos += 1
                else:
                    i += 1
            i = 0

            while numcard > 0:
                while i < len(self.hand):
                    if newhandpos >= len(newhand):
                        break
                    elif self.hand[i] == f'{numcard}':
                        newhand[newhandpos] = self.hand[i]
                        self.hand[i] = ""
                        i = 0
                        newhandpos += 1
                    else:
                        i += 1
                numcard -= 1
                i = 0
            i = 0
            while i < len(self.hand):
                if newhandpos >= len(newhand):
                    break
                elif self.hand[i] == "Assassin" or self.hand[i] == "Thief":
                    newhand[newhandpos] = self.hand[i]
                    self.hand[i] = ""
                    i = 0
                    newhandpos += 1
                else:
                    i += 1
        self.hand = newhand


class CommunityCards:
    def __init__(self):
        self.name="Community Cards"
        self.hand = list([])
        self.carddown = str("")

    def sort_hand(self):
        newhandpos = 0
        newhand = list(["", "", ""])
        numcard = 7
        i=0

        while newhandpos < len(newhand):
            while i < len(self.hand):
                if newhandpos >= 3:
                    break
                elif self.hand[i] == "F_King" or self.hand[i] == "M_King" or self.hand[i] == "S_King" or self.hand[i] == "D_King":
                    newhand[newhandpos] = self.hand[i]
                    self.hand[i] = ""
                    i = 0
                    newhandpos += 1
                else:
                    i += 1
            i=0
            while i < len(self.hand):
                if newhandpos >= 3:
                    break
                elif self.hand[i] == "F_Prince" or self.hand[i] == "M_Prince" or self.hand[i] == "S_Prince" or self.hand[i] == "D_Prince":
                    newhand[newhandpos] = self.hand[i]
                    self.hand[i] = ""
                    i = 0
                    newhandpos += 1
                else:
                    i += 1
            i = 0
            while i < len(self.hand):
                if newhandpos >= len(newhand):
                    break
                elif self.hand[i] == "F_Knight" or self.hand[i] == "M_Knight" or self.hand[i] == "S_Knight" or self.hand[i] == "D_Knight":
                    newhand[newhandpos] = self.hand[i]
                    self.hand[i] = ""
                    i = 0
                    newhandpos += 1
                else:
                    i += 1
            i = 0

            while numcard > 0:
                while i < len(self.hand):
                    if newhandpos >= 3:
                        break
                    elif self.hand[i] == f'{numcard}':
                        newhand[newhandpos] = self.hand[i]
                        self.hand[i] = ""
                        i = 0
                        newhandpos += 1
                    else:
                        i += 1
                numcard -= 1
                i = 0
            i = 0
            while i < len(self.hand):
                if newhandpos >= len(newhand):
                    break
                elif self.hand[i] == "Assassin" or self.hand[i] == "Thief":
                    newhand[newhandpos] = self.hand[i]
                    self.hand[i] = ""
                    i = 0
                    newhandpos += 1
                else:
                    i += 1
        self.hand = newhand


class HandClass:
    def __init__(self, classnames, frequency):
        self.name =classnames
        self.frequency = frequency


def deal(shuffleddeck, handbeingdealt, cardsdealt):
    hand = handbeingdealt
    hand.append(shuffleddeck[cardsdealt])
    return hand
