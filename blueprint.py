import random
from deck import deck

#this is the class module
class Player:
    def __init__ (self):
        self.hand = []
        self.max_cards = 7
        self.cards_in_play = []

    def play_random_card(self):
        card = random.choice(self.hand)
        self.cards_in_play.append(card)
        self.hand.remove(card)
        #print("Card in play is " + card.name)

        return None


class Card():
    def __init__(self, incoming_type, incoming_name, incoming_desc):
        self.name = incoming_name
        self.desc = incoming_desc
        self.type = incoming_type



class Herocard(Card):
    def __init__(self, incoming_type, incoming_name, incoming_desc, incoming_health, incoming_strength):
        self.health = incoming_health
        self.strength = incoming_strength
        super().__init__(incoming_type, incoming_name, incoming_desc)

    def herocard_actions(self, card_strength):
        post_attack_health = self.health - card_strength

        return post_attack_health
    

class Spellcard(Card):
    def __init__(self, incoming_type, incoming_name, incoming_desc, incoming_strength):
        self.strength = incoming_strength
        super().__init__(incoming_type, incoming_name, incoming_desc)

    def spellcard_actions(self, defending_health):
        post_spell_health = defending_health - self.strength

        return post_spell_health

class Buffcard(Card):
    def __init__(self, incoming_type, incoming_name, incoming_desc, incoming_health):
        self.health = incoming_health
        super().__init__(incoming_type, incoming_name, incoming_desc)

    def buffcard_actions(self, current_card_health):
        post_buff_health = current_card_health + self.health

        return post_buff_health 


