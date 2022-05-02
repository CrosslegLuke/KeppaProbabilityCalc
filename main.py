import gamecontrol


game1 = gamecontrol.GameMaster
player1 = gamecontrol.Player("Luke")
player2 = gamecontrol.Player("Brandon")
player3 = gamecontrol.Player("Chad")
player4 = gamecontrol.Player("Jonah")
player5 = gamecontrol.Player("Jay")
player6 = gamecontrol.Player("Mackey")
player7 = gamecontrol.Player("Kora")
player8 = gamecontrol.Player("Dara")


playernum = 8
cardsdealt = 0
playerbeingdealt=0
dealinground = 0

deck = gamecontrol.PlayerKylo().shuffle()

match playernum:
    case 2:
        while dealinground < 4:
            player1.hand = gamecontrol.deal(deck, player1.hand, cardsdealt)
            cardsdealt += 1
            player2.hand =gamecontrol.deal(deck, player2.hand, cardsdealt)
            cardsdealt += 1
            dealinground +=1
    case 3:
        while dealinground < 4:
            player1.hand = gamecontrol.deal(deck, player1.hand, cardsdealt)
            cardsdealt += 1
            player2.hand = gamecontrol.deal(deck, player2.hand, cardsdealt)
            cardsdealt += 1
            player3.hand = gamecontrol.deal(deck, player3.hand, cardsdealt)
            cardsdealt += 1
            dealinground += 1
    case 4:
        while dealinground < 4:
            player1.hand = gamecontrol.deal(deck, player1.hand, cardsdealt)
            cardsdealt += 1
            player2.hand = gamecontrol.deal(deck, player2.hand, cardsdealt)
            cardsdealt += 1
            player3.hand = gamecontrol.deal(deck, player3.hand, cardsdealt)
            cardsdealt += 1
            player4.hand = gamecontrol.deal(deck, player4.hand, cardsdealt)
            cardsdealt += 1
            dealinground += 1
    case 5:
        while dealinground < 4:
            player1.hand = gamecontrol.deal(deck, player1.hand, cardsdealt)
            cardsdealt += 1
            player2.hand = gamecontrol.deal(deck, player2.hand, cardsdealt)
            cardsdealt += 1
            player3.hand = gamecontrol.deal(deck, player3.hand, cardsdealt)
            cardsdealt += 1
            player4.hand = gamecontrol.deal(deck, player4.hand, cardsdealt)
            cardsdealt += 1
            player5.hand = gamecontrol.deal(deck, player5.hand, cardsdealt)
            cardsdealt += 1
            dealinground += 1
    case 6:
        while dealinground < 4:
            player1.hand = gamecontrol.deal(deck, player1.hand, cardsdealt)
            cardsdealt += 1
            player2.hand = gamecontrol.deal(deck, player2.hand, cardsdealt)
            cardsdealt += 1
            player3.hand = gamecontrol.deal(deck, player3.hand, cardsdealt)
            cardsdealt += 1
            player3.hand = gamecontrol.deal(deck, player3.hand, cardsdealt)
            cardsdealt += 1
            player4.hand = gamecontrol.deal(deck, player4.hand, cardsdealt)
            cardsdealt += 1
            player5.hand = gamecontrol.deal(deck, player5.hand, cardsdealt)
            cardsdealt += 1
            player6.hand = gamecontrol.deal(deck, player6.hand, cardsdealt)
            cardsdealt += 1
            dealinground += 1
    case 7:
        while dealinground < 4:
            player1.hand = gamecontrol.deal(deck, player1.hand, cardsdealt)
            cardsdealt += 1
            player2.hand = gamecontrol.deal(deck, player2.hand, cardsdealt)
            cardsdealt += 1
            player3.hand = gamecontrol.deal(deck, player3.hand, cardsdealt)
            cardsdealt += 1
            player4.hand = gamecontrol.deal(deck, player4.hand, cardsdealt)
            cardsdealt += 1
            player5.hand = gamecontrol.deal(deck, player5.hand, cardsdealt)
            cardsdealt += 1
            player6.hand = gamecontrol.deal(deck, player6.hand, cardsdealt)
            cardsdealt += 1
            player7.hand = gamecontrol.deal(deck, player7.hand, cardsdealt)
            cardsdealt += 1
            dealinground += 1
    case 8:
        while dealinground < 4:
            player1.hand = gamecontrol.deal(deck, player1.hand, cardsdealt)
            cardsdealt += 1
            player2.hand = gamecontrol.deal(deck, player2.hand, cardsdealt)
            cardsdealt += 1
            player3.hand = gamecontrol.deal(deck, player3.hand, cardsdealt)
            cardsdealt += 1
            player4.hand = gamecontrol.deal(deck, player4.hand, cardsdealt)
            cardsdealt += 1
            player5.hand = gamecontrol.deal(deck, player5.hand, cardsdealt)
            cardsdealt += 1
            player6.hand = gamecontrol.deal(deck, player6.hand, cardsdealt)
            cardsdealt += 1
            player7.hand = gamecontrol.deal(deck, player7.hand, cardsdealt)
            cardsdealt += 1
            player8.hand = gamecontrol.deal(deck, player8.hand, cardsdealt)
            cardsdealt += 1
            dealinground += 1

print(player1.hand)
print(player2.hand)
print(player3.hand)
print(player4.hand)
print(player5.hand)
print(player6.hand)
print(player7.hand)
print(player8.hand)