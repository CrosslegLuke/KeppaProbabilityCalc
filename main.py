import gamecontrol
numran =1
numrun = 1000000

HandsPlayed = {
    "GamesRan": 0, "T7s": 0, "RStr": 0, "TKings": 0, "TPrinces": 0, "TKnights": 0, "DKings": 0, "DPrinces": 0,
    "DKnights": 0, "T6s": 0, "Trips": 0, "NumStr": 0, "NumPairs": 0, "AllStraights": 0, "AllTrips": 0, "AllPairs": 0,
    "AllRoyalTrips": 0, "AllRoyalPairs": 0}


while numran <= numrun:
    game1 = gamecontrol.GameMaster

    HandsPlayed["GamesRan"] = HandsPlayed["GamesRan"]+1

    player1 = gamecontrol.Player("Luke")
    player2 = gamecontrol.Player("Brandon")
    player3 = gamecontrol.Player("Chad")
    player4 = gamecontrol.Player("Jonah")
    player5 = gamecontrol.Player("Jay")
    player6 = gamecontrol.Player("Mackey")
    player7 = gamecontrol.Player("Kora")
    player8 = gamecontrol.Player("Dara")
    community = gamecontrol.CommunityCards()


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
                player2.hand = gamecontrol.deal(deck, player2.hand, cardsdealt)
                cardsdealt += 1
                dealinground += 1

                if dealinground is not 4:
                    community.hand = gamecontrol.deal(deck, community.hand, cardsdealt)
                    cardsdealt += 1
        case 3:
            while dealinground < 4:
                player1.hand = gamecontrol.deal(deck, player1.hand, cardsdealt)
                cardsdealt += 1
                player2.hand = gamecontrol.deal(deck, player2.hand, cardsdealt)
                cardsdealt += 1
                player3.hand = gamecontrol.deal(deck, player3.hand, cardsdealt)
                cardsdealt += 1
                dealinground += 1

                if dealinground is not 4:
                    community.hand = gamecontrol.deal(deck, community.hand, cardsdealt)
                    cardsdealt += 1
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

                if dealinground is not 4:
                    community.hand = gamecontrol.deal(deck, community.hand, cardsdealt)
                    cardsdealt += 1
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

                if dealinground is not 4:
                    community.hand = gamecontrol.deal(deck, community.hand, cardsdealt)
                    cardsdealt += 1
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

                if dealinground is not 4:
                    community.hand = gamecontrol.deal(deck, community.hand, cardsdealt)
                    cardsdealt += 1
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

                if dealinground is not 4:
                    community.hand = gamecontrol.deal(deck, community.hand, cardsdealt)
                    cardsdealt += 1
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

                if dealinground is not 4:
                    community.hand = gamecontrol.deal(deck, community.hand, cardsdealt)
                    cardsdealt += 1

    player1.sort_hand()
    player2.sort_hand()
    player3.sort_hand()
    player4.sort_hand()
    player5.sort_hand()
    player6.sort_hand()
    player7.sort_hand()
    player8.sort_hand()
    community.sort_hand()
    #print("Community Cards: ", community.hand)


    table = gamecontrol.Table(community.hand, player1, player2, player3, player4, player5,
                          player6, player7, player8)

    table.build_true_hands()

    player1.sort_hand()
    player2.sort_hand()
    player3.sort_hand()
    player4.sort_hand()
    player5.sort_hand()
    player6.sort_hand()
    player7.sort_hand()
    player8.sort_hand()

    #print(player1.name, "'s hand: ", player1.hand)
    #print(player2.name, "'s hand: ", player2.hand)
    #print(player3.name, "'s hand: ", player3.hand)
    #print(player4.name, "'s hand: ", player4.hand)
    #print(player5.name, "'s hand: ", player5.hand)
    #print(player6.name, "'s hand: ", player6.hand)
    #print(player7.name, "'s hand: ", player7.hand)
    #print(player8.name, "'s hand: ", player8.hand)

    table.rate_hands(HandsPlayed)
    print("Games Run:", numran, "/", numrun)
    numran += 1

print("\n","\n", HandsPlayed)

