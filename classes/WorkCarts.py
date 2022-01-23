
from typing import List
from classes.Game import Game
from classes.Player import Player

class WorkCarts(Game):

    def __init__(self, players: List[Player]):
        #se crea la baraja de cartas
        super().__init__(players,8,2,4,6,True)

    def verify_carts_round(self):
        if self.deck.get_length_deck() >= (self.carts_table + self.carts_player*self.cant_players):
            return True
        else:
            return False

    def initialize_round(self):
        if self.verify_carts_round():
            print("A punto de iniciar una nueva ronda")
            #se asignan cartas a la ronda
            self.assign_cards_round()
            #lanzar cartas a la mesa
            self.cards_the_table()
            return True
        else:
            print("Ya no hay cartas suficientes para repartir")
            print("el juego ha culminado")
            self.define_player_winner()
            return False


    #ver ultima carta de la baraja de los jugadores
    def get_last_cart_players(self):
        cant = 1
        for player in self.deck_carts_player:
            if(len(self.deck_carts_player[player]) > 0):
                print(player+" : "+self.deck_carts_player[player][len(self.deck_carts_player[player])-1].card_info_short())
                cant += 1

    #Llevar carta de la mesa y sumar las dos cartas a la baraja del jugador
    def remove_cart_table(self,name_player,index_cart):
        cart = None
        valor = False
        point = self.get_selec_value_deck_assign_carts_player(name_player,index_cart)
        cont = 0
        index_list = 0
        while cont < len(self.deck_carts_table):
            if(self.deck_carts_table[index_list].get_point() == point):
                cart = self.deck_carts_table.pop(index_list) #se quita carta de la mesa
                self.deck_carts_player[name_player].append(cart) #Se agrega carta de la mesa a baraja de cartas ganadas
                valor = True
            else:
                index_list+=1
            cont+=1

        #Agregar la carta solo en caso se encontro siquiera una con el mismo valor en la mesa
        if(valor):
            cart = self.deck_assign_carts_player[name_player].pop(index_cart) # se quita carta de la baraja de mano
            self.deck_carts_player[name_player].append(cart) #se agrega carta que eligio en el turno
        return valor
    
    # robar baraja de otro jugador
    def steal_carts_other_player(self,name_player,val_cart):
        tamanio = 0
        valor = self.get_selec_value_deck_assign_carts_player(name_player,val_cart)
        value = False
        for player in self.deck_carts_player:
            tamanio = len(self.deck_carts_player[player])
            if(player != name_player and tamanio > 0):
                if(self.deck_carts_player[player][tamanio-1].get_point() == valor):
                    # agregar todas las cartas al jugador
                    for i in range(tamanio):
                        self.deck_carts_player[name_player].append(self.deck_carts_player[player][i])
                    self.deck_carts_player[player] = []
                    print("se agregaron las cartas del otro jugador")

                    #agregar su propia carta
                    cart = self.deck_assign_carts_player[name_player].pop(val_cart) # se quita carta de la baraja de mano
                    self.deck_carts_player[name_player].append(cart) #se agrega carta que eligio en el turno
                    value = True
                    break
        return value
        