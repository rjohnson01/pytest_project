from blueprint import Player, Herocard, Spellcard, Buffcard
import random
from deck import deck


#Function to get the players input and play a selected card
def player_card_selection():
    player.play_random_card()
    print("Player card in play: ", str(player.cards_in_play[-1].name))

    return None


#Function for ai_player card-in-play analysis
def ai_player_card_selection():
    ai_player.play_random_card()
    print("AI card in play: ", str(ai_player.cards_in_play[-1].name))

    return None


#Function that builds the playable deck
def build_play_deck():
    build_deck = []
    for cards in deck:                                                              #Loop through all the card objects in the deck
        if cards["type"] == "hero":                                                 #Create Hero card object using the current card values
            build_deck.append(Herocard(cards["type"], cards["name"], cards["desc"], cards["health"], cards["str"]))
        elif cards["type"] == "spell":                                              #Create Spell card object using the current card values
            build_deck.append(Spellcard(cards["type"], cards["name"], cards["desc"], cards["str"]))
        elif cards["type"] == "buff":                                               #Create Buff card object using the current card values
            build_deck.append(Buffcard(cards["type"], cards["name"], cards["desc"], cards["health"]))

    return build_deck

#Function to automatically draw new card
def draw_new_card():
    drawn_card = play_deck.pop(random.randrange(0, len(play_deck)))

    return drawn_card


#Function to initially draw 7 cards from the initial deck-in-play
def fill_players_hand(deck_to_draw_from):
    drawn_hand = []
    for card_draw in range(0,7):                                                   #Loop through the deck-in-play 7 times
        card_position = random.randrange(0, len(deck_to_draw_from))                #Randomize the card position to select from the deck-in-play
        drawn_hand.append(deck_to_draw_from.pop(card_position))
    
    return drawn_hand


#Function to show the players current hand to the player
#Further UI if necessary can come later
def display_player_hand(playable_cards):
    displayed_hand = playable_cards
    for numbered_list, cards in enumerate(displayed_hand, 1):
        if cards.type == "hero":
            print(str(numbered_list) + ".", cards.name + ":", cards.desc, "Health:", str(cards.health), "Strength:", str(cards.strength))
            print()
        elif cards.type == "spell":
            print(str(numbered_list) + ".", cards.name + ":", cards.desc, "Attack Power:", str(cards.strength))
            print()
        elif cards.type == "buff":
            print(str(numbered_list) + ".", cards.name + ":", cards.desc, "Points:", str(cards.health))
            print()

    return None


def card_actions(attacking_card, defending_card):
    if attacking_card.type == "hero":
        defending_card.health = attacking_card.herocard_actions(attacking_card.strength)
        #print("DEBUG -- " + str(defending_card.health))
    elif attacking_card.type == "spell":
        defending_card.health = attacking_card.spellcard_actions(defending_card.health)
        #print("DEBUG -- " + str(defending_card.health))
    elif attacking_card.type == "buff":
        defending_card.health = attacking_card.buffcard_actions(attacking_card.health)
        #print("The new health is: " + str(defending_card.name) + str(defending_card.health))

    return None


def game_intro():
    print("|-----Card Battle Game-----|")
    print("There's a human player, and an AI player.  Each player draws 7 cards from the deck,")
    print("then randomly plays them one at a time against the other player's cards.  First one")
    print("to defeat all the other player's cards wins!" + "\n")

    return None


if __name__ == "__main__":
    player = Player()                                                                   #Create the human player
    ai_player = Player()                                                                #Create the ai player
    discard_deck = []                                                                   #Create the card discard deck

    play_deck = build_play_deck()                                                       #Build the deck the players will use, populated with card objects                                                                        #Builds the empty discard deck
    player.hand = fill_players_hand(play_deck)                                          #Call the function to draw cards and put them into the player's hand
    ai_player.hand = fill_players_hand(play_deck)                                       #Call the function to draw cards and put them into the ai_player's hand
    
    game_intro()

    print("Your current hand: ")
    display_player_hand(player.hand)
    
    print("Human plays a card...") #the human player plays a card, and stuff happens
    print("AI plays a card...") #the ai player plays a card, and stuff happens            ai_card = ai_player_card_selection()
    while True:
        player_card_selection()

        ai_player_card_selection()


        card_actions(player.cards_in_play[random.randrange(0, len(player.cards_in_play))], ai_player.cards_in_play[0])
        #print("DEBUG CARDS IN PLAY BEFORE: ")
        #for names in player.cards_in_play:
            #print(names.name)
        if ai_player.cards_in_play[0].health <= 0:
            del ai_player.cards_in_play[0]
        #print("CARDS IN PLAY AFTER: ")
        #for ai_names in ai_player.cards_in_play:
            #print(ai_names.name)
            #discard_deck.append(ai_removed_card)

        card_actions(ai_player.cards_in_play[0], player.cards_in_play[0])
        if player.cards_in_play[0].health <= 0:
            del player.cards_in_play[0]
            #discard_deck.append(player_removed_card)
        
        player_drawn_card = draw_new_card()                                                 #player draws a new card
        player.hand.append(player_drawn_card)                                               #player adds new card to hand
        
        ai_player_drawn_card = draw_new_card()                                              #ai_player draws a new card
        ai_player.hand.append(ai_player_drawn_card)                                         #ai_player adds new card to hand
        
        print("Your current hand: ")
        display_player_hand(player.hand)
        
        #print("DEBUG - Player's new card is " + player_drawn_card.name)
        #print("DEBUG - AI player new card is " + ai_player_drawn_card.name)

        #import pdb; pdb.set_trace()
        print("---end of line---")


#google introspection vs reflection in python
#remember dirs
