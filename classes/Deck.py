import random
from typing import List
from classes.Card import Card

class Deck:

    def __init__(self,amount_deck):
        self.deck = self.create_carts(amount_deck)

    def show_cards(self):
        for card in self.deck:
            card.card_info()

    def create_carts(self,amount_deck):
        aux = []
        print("cantidad de barajas :",amount_deck)
        #Create cards
        for c in range(amount_deck):
            for s in Card.get_suits():
                for i in range(1,14):
                    str_val = ""
                    if i == 1:
                        str_val = "As"
                    elif i == 11:
                        str_val = "Jota"
                    elif i == 12:
                        str_val = "Reina"
                    elif i == 13:
                        str_val = "Rey"
                    else:
                        str_val = str(i)
                    aux.append( Card( s , i , str_val ) )
        aux = Deck.random_deck(aux)
        return aux

    @staticmethod
    def random_deck(lista:List):
        aux = []
        num_random = 0
        while(len(lista) > 0):
            num_random = random.randint(0,len(lista)-1)
            aux.append(lista[num_random])
            lista.pop(num_random);
        return aux

    def get_deck(self):
        return self.deck

    def remove_cart(self):
        aux = self.deck.pop()
        return aux

    def get_length_deck(self):
        return len(self.deck)